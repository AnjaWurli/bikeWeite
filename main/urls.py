"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_LOCATION, admin.site.urls),
    path("", include("bike_weite.urls")),
] + static(  # type: ignore
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

if settings.SOCIALACCOUNT_PROVIDERS or 1:
    urlpatterns.append(path("accounts/", include("allauth.urls")))
