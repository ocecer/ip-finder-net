from re import template
from django.urls import path
from account.views import logOut, changePassword, editProfile, signup, ProileDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', auth_views.LoginView.as_view(
        template_name='pages/signin.html', next_page='blog'), name='signin'),
    path('logout', logOut, name='logout'),
    path('change-password', changePassword, name='change-password'),
    path('edit-profile', editProfile, name='edit-profile'),
    path('user/<str:username>', ProileDetailView.as_view(), name='profile'),
]
