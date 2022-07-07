from django.http import HttpResponse
from django.shortcuts import render
from ipapi import location

# Create your views here.


def index(request):
    search = request.POST.get('search')
    data = location(ip=search, output='json')
    context = {"data": data}
    return render(request, "iplookup/index.html", context)


def about(request):
    return render(request, "iplookup/about.html")


def contact(request):
    return render(request, "iplookup/contact.html")
