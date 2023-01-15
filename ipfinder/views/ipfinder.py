from django.shortcuts import render
from ipapi import location
import environ

env = environ.Env()


def ipfinder(request):
    IPAPI_KEY = env("IPAPI_KEY")
    mapbox_access_token = env("mapbox_access_token")

    search = request.POST.get('search')

    if search == "" or search == None:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            print("returning FORWARDED_FOR")
            ip = x_forwarded_for.split(',')[-1].strip()
            search = ip
        elif request.META.get('HTTP_X_REAL_IP'):
            print("returning REAL_IP")
            ip = request.META.get('HTTP_X_REAL_IP')
            search = ip
        else:
            print("returning REMOTE_ADDR")
            ip = request.META.get('REMOTE_ADDR')
            # search = ip  # Uncomment in production

    context = {}

    try:
        data = location(ip=search, key=IPAPI_KEY, output='json')
        data["utc_offset"] = data["utc_offset"][:3]+":"+data["utc_offset"][3:]
        # Print data for logging
        print(data)
        context = context.update({"data": data})
    except Exception as e:
        print(e)

    context = context.update({"mapbox_access_token": mapbox_access_token})

    return render(request, "pages/index.html", context)
