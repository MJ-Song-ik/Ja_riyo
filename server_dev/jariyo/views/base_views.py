from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User

def index(request): #입력으로 request를 받아들임.
    cur_user = request.user # request로 받아들인 user정보를 cur_user에 저장
    #Anonymous user인지 확인
    if cur_user.is_authenticated: #is_authenticated는 django user model에 정의된 attribute로 
                                  #AnonmousUser가 들어오면 False반환
                                  # 로그인이 될 때 실행되는 코드
        username = User.objects.get(username=request.user)
        #로그인 될 때 index.html 반환
        return render(request, 'jariyo/index.html', {'username':username})
    else:
        #anonymous user일 경우 login.html 반환
        return render(request, 'account/login.html')