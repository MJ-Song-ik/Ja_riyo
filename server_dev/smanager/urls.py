from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'smanager'

urlpatterns = [
    path('list/', login_required(views.ShopView.as_view()), name='list'),
    path('create/', login_required(views.ShopCreateView.as_view()), name='create'),
    path('update/<int:s_id>', login_required(views.ShopUpdateView.as_view()), name='update'),
]