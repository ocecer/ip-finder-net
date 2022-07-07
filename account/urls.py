from django.urls import path, include
from . import views

urlpatterns = [
    path("signin", views.signin_request, name="signin"),
    path("signup", views.signup_request, name="signup"),
    path("logout", views.logout_request, name="logout"),
]
