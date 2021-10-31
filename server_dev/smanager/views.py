from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import View
from django.core.paginator import Paginator
from .forms import SeatUpdateForm, ShopCreateForm, ShopUpdateForm
from jariyo.models import Shop
from django.contrib import messages

class ShopView(View):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk) # 로그인중인 사용자 객체를 얻어옴

            # 조회
        if user.profile.ismanager:
            shop_list = user.shop_set.all() # 나의 가게만

            # 페이징처리
            page = request.GET.get('page') # 페이지 번호 알아오기
            if page is None:
                    page = 1
            else:
                    page = int(page)
            paginator = Paginator(shop_list, 1)  # 페이지당 1개씩 보여주기
            page_obj = paginator.get_page(page)
            context = {'shop_list': page_obj}

            return render(request, 'smanager/list.html', context)
        else:
            return redirect(request, 'jariyo:main')

    def post(self, request):
        u = User.objects.get(id=request.user.pk)
        s = get_object_or_404(u.shop_set.filter(name=request.POST.get('name')))

        form = SeatUpdateForm(request.POST, request.FILES, instance=s)

        if form.is_valid():
            seat = form.save(commit=False)
            seat.save()
            user = get_object_or_404(User, pk=request.user.pk)
            if user.profile.ismanager:
                shop_list = user.shop_set.all()
                page = int(request.GET.get('page'))
                paginator = Paginator(shop_list, 1)
                page_obj = paginator.get_page(page)
                context = {'shop_list': page_obj}

                return render(request, 'smanager/list.html', context)
        else:
            return redirect(request, 'smanager:list')

class ShopCreateView(View):
    def post(self, request):
        form = ShopCreateForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.manager = request.user
            shop.save()
        return redirect('smanager:list')

    def get(self, request):
        form = ShopCreateForm()
        content = {'form': form}
        return render(request, 'smanager/create.html', content)

class ShopUpdateView(View):
    def post(self, request, s_id):
        u = User.objects.get(id=request.user.pk)
        s = Shop.objects.get(id=s_id)
        if u == s.manager:
            form = ShopUpdateForm(request.POST, request.FILES, instance=s)
            if form.is_valid():
                shop = form.save(commit=False)
                shop.manager = u
                shop.save()
            return redirect('smanager:list')
        else:
            return redirect(request, 'jariyo:main')

    def get(self, request, s_id):
        form = ShopUpdateForm()
        shop = Shop.objects.get(id=s_id)
        u = User.objects.get(id=request.user.pk)
        if u == shop.manager:
            content = {
                'form': form,
                'shop': shop,
                }
            return render(request, 'smanager/update.html', content)
        else:
            return redirect(request, 'jariyo:main')