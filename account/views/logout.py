from django.contrib.auth import logout
from django.shortcuts import redirect


def logOut(request):
    logout(request)
    return redirect('blog')
