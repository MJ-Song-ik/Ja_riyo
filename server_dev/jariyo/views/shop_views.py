from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from jariyo.models import Shop
from django.views import View
from django.core.paginator import Paginator
import json

class StatusView(DetailView):
    model = Shop
    template_name = 'jariyo/status.html'

class MapView(View):
    def get(self, request):
        shop_list = Shop.objects.all()
        shopdict = []
        for shop in shop_list:
            content = {
                "name": shop.name,
                "latitude": shop.latitude,
                "longitude": shop.longitude,
                "type": shop.shop_type,
            }
            shopdict.append(content)
        shopJson = json.dumps(shopdict)
        page = request.GET.get('page') # 페이지 번호 알아오기
        if page is None:
                page = 1
        else:
                page = int(page)
        paginator = Paginator(shop_list, 10)
        page_obj = paginator.get_page(page)
        context = {
                'shop_list': page_obj,
                'shopJson': shopJson,
                }
        return render(request, 'jariyo/map.html', context)

class RestaurantView(View):
    def get(self, request):
        shop_list = Shop.objects.filter(shop_type="R")

        # 페이징처리
        page = request.GET.get('page') # 페이지 번호 알아오기
        if page is None:
                page = 1
        else:
                page = int(page)
        paginator = Paginator(shop_list, 10)
        page_obj = paginator.get_page(page)
        context = {'shop_list': page_obj}

        return render(request, 'jariyo/list.html', context)

class CafeView(View):
    def get(self, request):
        shop_list = Shop.objects.filter(shop_type="C")

        # 페이징처리
        page = request.GET.get('page') # 페이지 번호 알아오기
        if page is None:
                page = 1
        else:
                page = int(page)
        paginator = Paginator(shop_list, 10)
        page_obj = paginator.get_page(page)
        context = {'shop_list': page_obj}

        return render(request, 'jariyo/list.html', context)