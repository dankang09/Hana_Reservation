from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    # path('', views.booking, name='booking-list'),
    # path('', views.BookingView.as_view(), name='booking-list'),
    path("users/<int:user_id>/", views.ProfileView.as_view(), name="profile"),

    path('<int:booking_id>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('branch/<int:booking_id>/delete/', views.BookingDeleteView.as_view(), name='booking-delete'),

    path('branch/', views.BranchView.as_view(), name='branch-list'),
    path('branch/search/', views.SearchView.as_view(), name='search'),
    path('branch/<int:branch_id>/create/', views.BookingCreateView.as_view(), name="booking-create"),
    
]