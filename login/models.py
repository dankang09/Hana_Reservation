from django.db import models
from django.contrib.auth.models import AbstractUser
# from .validators import validate_no_special_characters

# Create your models here.

class User(AbstractUser):
    # 회원가입시 커스텀필드 추가하고 싶을 때
    name = models.CharField(
        max_length=15, 
        unique=False, 
        null=True,
        # error_messages={"unique": "이미 사용 중인 닉네임입니다."}
        ) 

    def __str__(self):
        return self.email