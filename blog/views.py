from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category

# Create your views here.


def blog(request):
    context = {
        "blogs": Blog.objects.filter(is_verified=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blog.html", context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-detail.html", {"blog": blog})


def category_list(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_verified=True),
        # "blogs": Blog.objects.filter(is_verified=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blog.html", context)
