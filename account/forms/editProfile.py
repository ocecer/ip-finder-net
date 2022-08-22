from dataclasses import field
from distutils.sysconfig import customize_compiler
from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUserModel


class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUserModel
        fields = ('email', 'first_name', 'last_name', 'avatar')
