from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    url(r'^profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileView.as_view()), name='profile'),
    path('profile_update/', login_required(views.ProfileUpdateView.as_view()), name='profile_update'),
]