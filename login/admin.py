from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("name",)}),) # 회원가입시 커스텀필드 추가하고 싶을 때