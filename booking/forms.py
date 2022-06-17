# socket 호출하면 에러남.. 이유 알 수 없음. socket이 무슨 역할인지도 알 수 없음
# from socket import fromshare
from django import forms
from booking.models import Booking, Comment, Branch, BookingComment
import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "booking_dates",
            "booking_times",
            "booking_task",
            "booking_etc",
            "booking_image1",
            "booking_image2",
            "booking_image3",
            # "booking_employee",
        ]
        widgets = {
            # "booking_dates": forms.SelectDateWidget(years=["2022"],),
            "booking_dates": forms.DateInput(format=('%m/%d/%Y'),
                attrs={'class':'form-control', 'placeholder':'날짜를 선택해주세요!', 'type':'date'}),
            # "booking_times": forms.Select,
            # "booking_task": forms.SelectMultiple,
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea,
        }


class BookingCommentForm(forms.ModelForm):
    class Meta:
        model = BookingComment
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea,
        }


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = [
            "branch_name",
            "branch_num",
            "branch_tel",
            "branch_address",
            "branch_image",
            "branch_link",
        ]
        # widgets = {
        #     "intro": forms.Textarea
        # }