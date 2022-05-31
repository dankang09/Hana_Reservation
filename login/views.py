from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView


# Create your views here.

def index(request):
    return render(request, "login/index.html")

# 비밀번호 변경 시 바로 booking 화면으로 이동(오버라이팅))
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("booking:profile")

