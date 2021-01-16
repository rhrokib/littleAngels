from django.shortcuts import render
from django.http import HttpResponse
from .models import EmergencyLink
from django.views.generic import ListView


class PostListView(ListView):
    model = EmergencyLink
    template_name = 'emergency/emergency.html'
    context_object_name = 'posts'
    ordering = ['location']
    paginate_by = 5
