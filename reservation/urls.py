"""reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from login.views import CustomPasswordChangeView

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # login
    path('', include("login.urls")),

    # booking
    path('booking/', include("booking.urls")),
    
    # Allauth
    path("email-confirmation-done/",
        TemplateView.as_view(template_name = "login/email_confirmation_done.html"),
        name = "account_email_confirmation_done"
        ),
    path("password/change/", 
        CustomPasswordChangeView.as_view(), 
        name = "account_password_change",
        ), # allauth에 있는 password_change의 url을 오버라이팅
    path("naver/login/booking",
        TemplateView.as_view(template_name = "booking/booking.html"),
        name="naver_login_done"
        ),  # 네이버 로그인 성공시
    path("kakao/login/booking",
        TemplateView.as_view(template_name = "booking/booking.html"),
        name="kakao_login_done"
        ),  # 카카오 로그인 성공시
    path('', include('allauth.urls')),
    # path('accounts/', include('allauth.urls')),
    
]
