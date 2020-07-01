"""Post urls"""

#Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    
    path(
        route='',
        view=views.PostsFeedViews.as_view(), 
        name='feed'),
    path(
        route='posts/new',
        view=views.CreatePostView.as_view(), 
        name='create_post'),
    path(
        route='posts/<int:pk>',
        view=views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        route='post/like/<int:pk>',
        view=views.LikePostView.as_view(),
        name='like_post'
    )
]