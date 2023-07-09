"""URLs of the bike_weite django app."""
from bike_weite import views

from django.urls import path

urlpatterns = [
    path("", views.index, name="index")
]
