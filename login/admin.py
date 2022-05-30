from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

admin.site.register(User, UserAdmin)

# 관리자 페이지에 커스텀필드 추가
UserAdmin.fieldsets += (
    ("Custom fields", {"fields": ("name", "phone", "profile_pic", "intro")}),
)