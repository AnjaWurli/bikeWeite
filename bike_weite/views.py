from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """Return the App"""
    return render(request, template_name="bike_weite/index.html")


@login_required
@cache_page(60 * 15)
def get_map(request):
    """Get a map to visualize the distance"""
    import geopandas as gpd
    import networkx as nx
    import numpy as np
    import osmnx as ox
    import os.path as osp
    import tempfile
    import folium
    import hashlib
    from shapely.geometry import LineString
    from shapely.geometry import Point
    from shapely.geometry import Polygon

    cache_folder = osp.join(tempfile.gettempdir(), "osmnx_cache")

    ox.settings.cache_folder = cache_folder

    place = request.GET.get("address", "Geesthacht, Germany")

    point = ox.geocoder.geocode(place)

    network_type = "drive"
    # rc[:]["network_type"] = network_type
    distance = float(request.GET.get("distance"))

    if distance > 30:
        return HttpResponseBadRequest()
    distance *= 1000
    distances = np.linspace(0, distance, 6)[1:]

    md5 = hashlib.md5(place.encode("utf-8")).hexdigest()
    graph_file = osp.join(cache_folder, md5 + ".graphml")

    if not osp.exists(graph_file):
        G = ox.graph_from_point(
            point, network_type=network_type, dist=max(20000, distance)
        )
        ox.save_graphml(G, graph_file)
    else:
        G = ox.load_graphml(graph_file)

    center_node = ox.distance.nearest_nodes(G, point[1], point[0])
    G = ox.project_graph(G)
    graph_nodes = ox.graph_to_gdfs(G, edges=False)

    # get one color for each isochrone
    iso_colors = ox.plot.get_colors(
        n=len(distances), cmap="plasma", start=0, return_hex=True
    )

    def make_iso_polys(G, edge_buff=25, node_buff=50, infill=False):
        isochrone_polys = []
        for distance in sorted(distances, reverse=True):
            subgraph = nx.ego_graph(
                G, center_node, radius=distance, distance="length"
            )

            node_points = [
                Point((data["x"], data["y"]))
                for node, data in subgraph.nodes(data=True)
            ]
            nodes_gdf = gpd.GeoDataFrame(
                {"id": list(subgraph.nodes)}, geometry=node_points
            )
            nodes_gdf = nodes_gdf.set_index("id")

            edge_lines = []
            for n_fr, n_to in subgraph.edges():
                f = nodes_gdf.loc[n_fr].geometry
                t = nodes_gdf.loc[n_to].geometry
                edge_lookup = G.get_edge_data(n_fr, n_to)[0].get(
                    "geometry", LineString([f, t])
                )
                edge_lines.append(edge_lookup)

            n = nodes_gdf.buffer(node_buff).geometry
            e = gpd.GeoSeries(edge_lines).buffer(edge_buff).geometry
            all_gs = list(n) + list(e)
            new_iso = gpd.GeoSeries(all_gs).unary_union

            # try to fill in surrounded areas so shapes will appear solid and
            # blocks without white space inside them
            if infill:
                new_iso = Polygon(new_iso.exterior)
            isochrone_polys.append(new_iso)

        return isochrone_polys

    # make the isochrone polygons
    isochrone_polys = make_iso_polys(G, edge_buff=25, node_buff=0, infill=True)
    gdf = gpd.GeoDataFrame(geometry=isochrone_polys, crs=graph_nodes.crs)
    gdf["within distance to %s (in km)" % place] = distances[::-1] / 1000.

    m = gdf.explore(color=iso_colors, style_kwds=dict(fillOpacity=0.2))
    folium.Marker(point, popup="<b>%s</b>" % place).add_to(m)
    m.render()
    html = m._repr_html_()

    return HttpResponse(html)
