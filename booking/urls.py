from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    # profile, branch-update
    path("users/<int:user_id>/", views.ProfileView.as_view(), name="profile"),
    
    # booking
    path('<int:booking_id>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('<int:booking_id>/delete/', views.BookingDeleteView.as_view(), name='booking-delete'),

    # branch
    path('branch/', views.BranchView.as_view(), name='branch-list'),
    path('branch/search/', views.SearchView.as_view(), name='search'),
    path('branch/<int:branch_id>/', views.BranchDetailView.as_view(), name='branch-detail'),
    path('branch/<int:branch_id>/create/', views.BookingCreateView.as_view(), name="booking-create"),
    path("branch/<int:branch_id>/edit-branch/", views.BranchUpdateView.as_view(), name="branch-update"),
    
    # comment-branch
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

    # comment-booking
    path('<int:booking_id>/bookingcomments/create/',
        views.BookingCommentCreateView.as_view(),
        name='booking-comment-create',
    ),
    path('bookingcomments/<int:booking_comment_id>/edit/',
        views.BookingCommentUpdateView.as_view(),
        name='booking-comment-update'
    ),
    path('bookingcomments/<int:booking_comment_id>/delete/',
        views.BookingCommentDeleteView.as_view(),
        name='booking-comment-delete'
    ),

    # like
    path('like/<int:content_type_id>/<int:object_id>/',
        views.ProcessLikeView.as_view(),
        name='process-like'
    ),

    # follow
    path('branch/<int:branch_id>/follow/',
        views.ProcessFollowView.as_view(),
        name='process-follow'
    ),
    path('users/<int:user_id>/following/', 
        views.FollowingListView.as_view(), 
        name='following-list'
    ),
    path('branch/<int:branch_id>/followers/', 
        views.FollowerListView.as_view(), 
        name='follower-list'
    ),

]