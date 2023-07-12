from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Return the App"""
    return render(request, template_name="bike_weite/index.html")


def get_map(request):
    """Get a map to visualize the distance"""
    import geopandas as gpd
    import networkx as nx
    import numpy as np
    import osmnx as ox
    import os.path as osp
    import tempfile
    from branca.element import Figure
    from shapely.geometry import LineString
    from shapely.geometry import Point
    from shapely.geometry import Polygon

    place = request.GET.get("address", "Geesthacht, Germany")
    network_type = "drive"
    # rc[:]["network_type"] = network_type
    distance = float(request.GET.get("distance")) * 1000
    distances = np.linspace(0, distance, 6)[1:]

    G = ox.graph_from_place(place, network_type=network_type)
    gdf_nodes = ox.graph_to_gdfs(G, edges=False)

    x, y = gdf_nodes["geometry"].unary_union.centroid.xy
    center_node = ox.distance.nearest_nodes(G, x[0], y[0])
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

    m = gdf.explore(
        color=iso_colors, style_kwds=dict(fillOpacity=0.2), tooltip=False
    )
    m.render()
    html = m._repr_html_()

    # with tempfile.TemporaryDirectory() as tmpdir:
    #     mapfile = osp.join(tmpdir, "map.html")
    #     m.save(mapfile)
    #     with open(mapfile) as f:
    #         html = f.read()



    return HttpResponse(html)
