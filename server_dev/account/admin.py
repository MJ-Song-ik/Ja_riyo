from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Photo
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    con_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# 기존의 User의 등록을 취소했다가 User와 ProfileInline을 붙임.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Photo)