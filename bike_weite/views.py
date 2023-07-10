from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Return the App"""
    return render(request, template_name="bike_weite/index.html")


def get_map(request):
    """Get a map to visualize the distance"""
    return HttpResponse(
    """
    <h1>Input data of the request</h1>
    <ul>
    <li>address: %s</li>
    <li>distance: %s</li>
    </ul>
    """ % (request.GET.get("address", None), request.GET.get("distance"))
    )
