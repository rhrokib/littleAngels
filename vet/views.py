from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Vet
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from PIL import Image
import os
# Create your views here.


def home(request):
    context = {
        'posts': Vet.objects.all()
    }

    return render(request, 'vet/vet.html', context=context,)


class PostListView(LoginRequiredMixin, ListView):
    model = Vet
    template_name = 'vet/vet.html'
    context_object_name = 'posts'
    ordering = ['location']
    paginate_by = 5
    
    def get_queryset(self):
        p = Vet.objects.filter(approved=True)
        return p.order_by('location')


class UserPostListView(LoginRequiredMixin, ListView):
    model = Vet
    template_name = 'vet/vet_profile.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Vet.objects.filter(author=user).order_by('location')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Vet


# Creating and deletion
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Vet
    template_name = 'vet/vet_form.html'
    fields = ['institute', 'certification',
              'phone', 'location', 'content', 'work_hours', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = '/vet'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vet
    fields = ['institute', 'certification',
              'phone', 'location', 'work_hours', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vet

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = '/vet'

    # just checking
