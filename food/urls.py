from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='food'),
    path('post/<int:pk>', PostDetailView.as_view(), name='shop_detail'),
    path('new', PostCreateView.as_view(), name='shop_create'),
    path('updae/<int:pk>/update', PostUpdateView.as_view(), name='shop_update'),
    path('delete/<int:pk>/delete', PostDeleteView.as_view(), name='shop_delete'),
]