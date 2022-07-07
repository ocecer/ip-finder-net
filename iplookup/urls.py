from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    # path('', include('blog.urls'))
    # path("blog", views.blog),
    # path("blog/<str:id>", views.blog_detail)
]
