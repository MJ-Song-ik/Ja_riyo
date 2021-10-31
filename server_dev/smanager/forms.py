from django import forms
from jariyo.models import Shop

# Create your models here.

class ShopCreateForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)
    class Meta:
        model = Shop
        fields = [
            'name',
            'main_photo',
            'latitude',
            'longitude',
            'shop_type',
            'site',
            'sit_over4_max',
            'sit_4_max',
            'sit_2_max',
        ]
        labels = {
            'name': '가게이름',
            'main_photo': '사진',
            'latitude': '위도',
            'longitude': '경도',
            'shop_type': '카테고리',
            'site': '웹사이트 주소',
            'sit_over4_max': '4인이상 최대:',
            'sit_4_max': '4인석 최대:',
            'sit_2_max': '2인석 최대:',
        }  

class SeatUpdateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name',
            'sit_over4',
            'sit_4',
            'sit_2',
        ]

class ShopUpdateForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)
    class Meta:
        model = Shop
        fields = [
            'name',
            'main_photo',
            'latitude',
            'longitude',
            'shop_type',
            'site',
            'sit_over4_max',
            'sit_4_max',
            'sit_2_max',
        ]
        labels = {
            'name': '가게이름',
            'main_photo': '사진',
            'latitude': '위도',
            'longitude': '경도',
            'shop_type': '카테고리',
            'site': '웹사이트 주소',
            'sit_over4_max': '4인이상 최대:',
            'sit_4_max': '4인석 최대:',
            'sit_2_max': '2인석 최대:',
        }  
        