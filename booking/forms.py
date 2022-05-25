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