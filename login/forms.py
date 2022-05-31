from django import forms
from .models import User

# class SignupForm(forms.ModelForm): # 회원가입시 커스텀필드도 투입하게 하고 싶을 때
#     class Meta:
#         model = User
#         fields = ["name", "phone"]

#     def signup(self, request, user):
#         user.name = self.cleaned_data["name"]
#         user.phone = self.cleaned_data["phone"]
#         user.save()
# 프로필 설정페이지 구현하면서 주석처리함


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            "profile_pic",
            "phone",
            "intro",
        ]
        widgets = {
            "intro": forms.Textarea
        }