from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import EditProfileForm


@login_required(login_url='/')
def editProfile(request):
    if request.method == 'POST':
        form=EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile changed.")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'pages/edit-profile.html', context={'form': form})
