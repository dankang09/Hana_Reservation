from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path("users/<int:user_id>/", views.ProfileView.as_view(), name="profile"),

    # booking
    path('<int:booking_id>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('<int:booking_id>/delete/', views.BookingDeleteView.as_view(), name='booking-delete'),

    # branch
    path('branch/', views.BranchView.as_view(), name='branch-list'),
    path('branch/search/', views.SearchView.as_view(), name='search'),
    path('branch/<int:branch_id>/', views.BranchDetailView.as_view(), name='branch-detail'),
    path('branch/<int:branch_id>/create/', views.BookingCreateView.as_view(), name="booking-create"),
    
    # comment
    path('branch/<int:branch_id>/comments/create/',
        views.CommentCreateView.as_view(),
        name='comment-create',
    ),
    path('comments/<int:comment_id>/edit/',
        views.CommentUpdateView.as_view(),
        name='comment-update'
    ),
    path('comments/<int:comment_id>/delete/',
        views.CommentDeleteView.as_view(),
        name='comment-delete'
    ),
]