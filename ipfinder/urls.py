from django.urls import path
from .views.ipfinder import ipfinder

urlpatterns = [
    path("", ipfinder, name='home'),
]
