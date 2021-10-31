from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views import View
from .forms import UserForm, ProfileForm, UserCreation

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserCreation()
    return render(request, 'account/signup.html', {'form': form})

class ProfileView(DetailView):
    context_object_name = 'profile_user' # model로 지정해준 User모델에 대한 객체와 로그인한 사용자랑 명칭이 겹쳐버리기 때문에 이를 지정해줌.
    model = User
    template_name = 'account/profile.html'

class ProfileUpdateView(View): # 간단한 View클래스를 상속 받았으므로 get함수와 post함수를 각각 만들어줘야한다.
    # 프로필 편집에서 보여주기위한 get 메소드
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)  # 로그인중인 사용자 객체를 얻어옴
        user_form = UserForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

        if hasattr(user, 'profile'):  # user가 profile을 가지고 있으면 True, 없으면 False (회원가입을 한다고 profile을 가지고 있진 않으므로)
            profile = user.profile
            profile_form = ProfileForm(initial={
                'nickname': profile.nickname,
                'profile_photo': profile.profile_photo,
                'phone': profile.phone,
            })
        else:
            profile_form = ProfileForm()

        return render(request, 'account/profile_update.html', {"user_form": user_form, "profile_form": profile_form})

    # 프로필 편집에서 실제 수정(저장) 버튼을 눌렀을 때 넘겨받은 데이터를 저장하는 post 메소드
    def post(self, request):
        u = User.objects.get(id=request.user.pk)        # 로그인중인 사용자 객체를 얻어옴
        user_form = UserForm(request.POST, instance=u)  # 기존의 것의 업데이트하는 것 이므로 기존의 인스턴스를 넘겨줘야한다. 기존의 것을 가져와 수정하는 것

        # User 폼
        if user_form.is_valid():
            user_form.save()

        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile) # 기존의 것 가져와 수정하는 것
        else:
            profile_form = ProfileForm(request.POST, request.FILES) # 새로 만드는 것

        # Profile 폼
        if profile_form.is_valid():
            profile = profile_form.save(commit=False) # 기존의 것을 가져와 수정하는 경우가 아닌 새로 만든 경우 user를 지정해줘야 하므로
            profile.user = u
            profile.save()

        return redirect('account:profile', pk=request.user.pk) # 수정된 화면 보여주기