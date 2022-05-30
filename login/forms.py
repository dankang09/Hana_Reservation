from django import forms
from .models import User

class SignupForm(forms.ModelForm): # 회원가입시 커스텀필드 추가하고 싶을 때
    class Meta:
        model = User
        fields = ["name", "phone"]

    def signup(self, request, user):
        user.name = self.cleaned_data["name"]
        user.phone = self.cleaned_data["phone"]
        user.save()