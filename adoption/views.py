from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AdoptionPost
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView 
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from PIL import Image
import os



class PostListView(LoginRequiredMixin, ListView):
    model = AdoptionPost
    template_name = 'adoption/adoption.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5
    
    def get_queryset(self):
        p = AdoptionPost.objects.filter(approved=True)
        return p.order_by('-date')
        
    


class UserPostListView(LoginRequiredMixin, ListView):
    model = AdoptionPost
    template_name = 'adoption/user_adoption.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return AdoptionPost.objects.filter(author=user).order_by('-date')




class PostDetailView(LoginRequiredMixin, DetailView):
    model = AdoptionPost


# Creating and deletion
class PostCreateView(LoginRequiredMixin, CreateView):
    model = AdoptionPost
    fields = ['title', 'location', 'contact', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AdoptionPost
    fields = ['title', 'location', 'contact', 'content', 'isAdopted', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AdoptionPost

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = '/adoption'

    # just checkingAdoption