from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path("", views.index, name="index"),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
]