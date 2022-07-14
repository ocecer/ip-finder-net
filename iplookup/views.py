from os import getenv
from django.shortcuts import render
from ipapi import location

# Create your views here.


def index(request):
    search = request.POST.get('search')
    data = location(
        ip=search, key="MwaVWZaqDrA789CCFsXLDBj3EbCVqThDZAQSra801XfRg0siv3", output='json')
    # data={"ip":"8.8.8.8"}

    # if data["ip"] == "127.0.0.1" or data["ip"] == "192.64.117.254":
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if x_forwarded_for:
    #         print("returning FORWARDED_FOR")
    #         ip = x_forwarded_for.split(',')[-1].strip()
    #         # search = ip
    #     elif request.META.get('HTTP_X_REAL_IP'):
    #         print("returning REAL_IP")
    #         ip = request.META.get('HTTP_X_REAL_IP')
    #         # search = ip
    #     else:
    #         print("returning REMOTE_ADDR")
    #         ip = request.META.get('REMOTE_ADDR')
    #         # search = ip
    # else:
    #     pass

    # data = location(
    #     ip=search, key="MwaVWZaqDrA789CCFsXLDBj3EbCVqThDZAQSra801XfRg0siv3", output='json')
    context = {"data": data}

    mapbox_access_token = "pk.eyJ1Ijoib2NlY2VyIiwiYSI6ImNsNWplbWpuNjBoYXgzanBsN2YxYmtiNWYifQ.1DkXiiu0jy5L9OQ2zYXsAw"
    context.update({"mapbox_access_token": mapbox_access_token})

    print(data)
    return render(request, "iplookup/index.html", context)


def about(request):
    return render(request, "iplookup/about.html")


def contact(request):
    return render(request, "iplookup/contact.html")
