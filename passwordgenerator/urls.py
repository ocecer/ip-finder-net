from django.urls import path
from .views import create_password

urlpatterns = [
    path("", create_password, name='password-generator'),
]
