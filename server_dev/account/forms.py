from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreation(UserCreationForm):
    email = forms.EmailField(label="이메일")
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ('nickname', 'profile_photo', 'phone')