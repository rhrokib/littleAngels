from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='vet'),
    # path('<str:username>', UserPostListView.as_view(), name='vet_profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='vet_post_detail'),
    path('new', PostCreateView.as_view(), name='vet_post_create'),
    path('vet_profile/<int:pk>/update', PostUpdateView.as_view(), name='vet_post_update'),
    path('vet_profile/<int:pk>/delete', PostDeleteView.as_view(), name='vet_post_delete'),
]