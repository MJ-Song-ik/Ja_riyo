from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User

def index(request):
    cur_user = request.user
    
    if cur_user.is_authenticated:
        username = User.objects.get(username=request.user)
        return render(request, 'jariyo/index.html', {'username':username})
    else:
        return render(request, 'account/login.html')