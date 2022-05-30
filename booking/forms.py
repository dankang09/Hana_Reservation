# socket 호출하면 에러남.. 이유 알 수 없음. socket이 무슨 역할인지도 알 수 없음
# from socket import fromshare
from django import forms
from booking.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "booking_dates",
            "booking_times",
            "booking_task",
            "booking_etc",
        ]
        widgets = {
            "booking_times": forms.RadioSelect,
            "booking_task": forms.RadioSelect,
        }