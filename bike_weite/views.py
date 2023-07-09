from django.shortcuts import render

# Create your views here.
def index(request):
    """Return the App"""
    return render(request, template_name="bike_weite/index.html")