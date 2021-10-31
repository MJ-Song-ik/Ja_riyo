from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url
from .views import base_views, shop_views
from django.shortcuts import render

app_name = 'jariyo'

urlpatterns = [
    # base_views.py
    path('main/', base_views.index, name='main'),
    path('map/', login_required(shop_views.MapView.as_view()), name='map'),
    path('restaurant/', login_required(shop_views.RestaurantView.as_view()), name='restaurant'),
    path('cafe/', login_required(shop_views.CafeView.as_view()), name='cafe'),
    url(r'^status/(?P<pk>[0-9]+)/$', login_required(shop_views.StatusView.as_view()), name='status'),
]