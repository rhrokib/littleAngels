from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='adoption'),
    path('postby_<str:username>', UserPostListView.as_view(), name='adoption_user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='adoption_post_detail'),
    path('new', PostCreateView.as_view(), name='adoption_post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='adoption_post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='adoption_post_delete'),
]
