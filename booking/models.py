from django.db import models
from .validators import validate_branch_link
from login.models import User

# 제네릭 관계 구현(좋아요기능)
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=20)
    branch_num = models.CharField(max_length=4)
    branch_tel = models.CharField(max_length=11)
    branch_address = models.TextField()
    branch_image = models.ImageField(upload_to="branch_pics", blank=True)
    branch_link = models.URLField(validators=[validate_branch_link], blank=True)
    likes = GenericRelation('Like')

    def __str__(self):
        return self.branch_name + '(' + str(self.branch_num) + ')'


class Booking(models.Model):
    TIME_CHOICES = [
        (1, "09:00"),
        (2, "09:30"),
        (3, "10:00"),
        (4, "10:30"),
        (5, "11:00"),
        (6, "11:30"),
        (7, "12:00"),
        (8, "12:30"),
        (9, "13:00"),
        (10, "13:30"),
        (11, "14:00"),
        (12, "14:30"),
        (13, "15:00"),
        (14, "15:30"),
    ]
    
    TASK_CHOICES = [
        (1, "개인/가계 예금(수신)업무"),
        (2, "개인/가계 대출(여신)업무"),
        (3, "개인/가계 외환"),
        (4, "기업 예금(수신)업무"),
        (5, "기업 대출(여신)업무"),
        (6, "기업 외환")
    ]

    booking_dates = models.DateField()
    booking_times = models.IntegerField(choices=TIME_CHOICES, default=None)
    booking_task = models.IntegerField(choices=TASK_CHOICES, default=None)
    booking_etc = models.TextField()
    booking_dt_created = models.DateTimeField(auto_now_add=True)

    #역관계, user.bookings 로 접근 가능
    booking_client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    #역관계, branch.bookings 로 접근 가능
    booking_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='bookings')
    

class Comment(models.Model):
    content = models.TextField(max_length=200, blank=False)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    
    #역관계, user.comments 로 접근 가능
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    #역관계, branch.comments 로 접근 가능
    comment_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='comments')
    likes = GenericRelation('Like')

    def __str__(self):
        return self.content[:30]

    class Meta:
        ordering = ['-dt_created']


class Like(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    #content_type은 직접 접근할 일이 없어서 역관계 설정 안함
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    
    #기본적으로 GenericForeignKey는 on_delete 옵션의 CASCADE가 적용되지 않음
    #Branch와 Comment 모델에서 Likes 필드(GenericRelation)을 통해 CASCADE와 동일한 효과 발생 
    liked_obejct = GenericForeignKey()

    def __str__(self):
        return f"({self.user}, {self.liked_obejct})"