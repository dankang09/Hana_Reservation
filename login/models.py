from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
# import booking.models

# Create your models here.

class User(AbstractUser):
    # 회원가입시 커스텀필드 추가하고 싶을 때
    name = models.CharField(
        max_length=15, 
        unique=False, 
        null=True,
        validators=[validate_no_special_characters],
        # error_messages={"unique": "이미 사용 중인 닉네임입니다."}
    )
    
    phone = models.CharField(
        max_length=11,
        unique=True,
        null=True,
    )

    profile_pic = models.ImageField(
        default="default_profile_pic.jpg", upload_to="profile_pics"
    )
    
    intro = models.CharField(max_length=60, blank=True)

    following = models.ManyToManyField('booking.Branch', blank=True, related_name='followers')

    def __str__(self):
        return self.email