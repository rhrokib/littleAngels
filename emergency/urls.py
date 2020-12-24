from django.urls import path
from . import views

urlpatterns = [
    path('', views.emergency, name='emergency'),
]