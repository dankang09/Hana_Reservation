from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView

# 프로필 수정 페이지 세팅
from .models import User
from django.views.generic import UpdateView
from .forms import ProfileForm
from braces.views import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def index(request):
    return render(request, "login/index.html")

# 비밀번호 변경 시 바로 booking 화면으로 이동(오버라이팅))
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        user = self.request.user
        return reverse("booking:profile", args=[user.id])

# 프로필 설정
class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "login/profile_set_form.html"

    # 업데이트 해야할 오브젝트(유저)가 뭔지 UpdateView에게 알려주기(오버라이드)
    # 하나의 오브젝트를 다루는 DetailView, DeleteView, CreateView 는 get_object를 오버라이드 할 수 있음
    # 그 외에 여러개의 오브젝트를 다루는 뷰에서는 get_queryset을 오버라이드 해야함
    def get_object(self, queryset=None):
        # 현재 유저 가져오기
        return self.request.user

    def get_success_url(self):
        user = self.request.user
        return reverse("booking:profile", args=[user.id])


# 프로필 수정
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "login/profile_set_form.html"

    # 업데이트 해야할 오브젝트(유저)가 뭔지 UpdateView에게 알려주기(오버라이드)
    # 하나의 오브젝트를 다루는 DetailView, DeleteView, CreateView 는 get_object를 오버라이드 할 수 있음
    # 그 외에 여러개의 오브젝트를 다루는 뷰에서는 get_queryset을 오버라이드 해야함
    def get_object(self, queryset=None):
        # 현재 유저 가져오기
        return self.request.user

    def get_success_url(self):
        user = self.request.user
        return reverse("booking:profile", args=[user.id])