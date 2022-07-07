from django.urls import path, include
from . import views

urlpatterns = [
    path("blog", views.blog, name="blog"),
    path("category/<slug:slug>", views.category_list, name="category_list"),
    path("blog/<slug:slug>", views.blog_detail, name="blog_detail")
]
