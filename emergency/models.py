from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import os
from django.utils import timezone


class EmergencyLink(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    location = models.CharField(max_length=50)
    work_hours = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    image = models.ImageField(default='default_emergency.png', upload_to='emergency_pics')

    def __str__(self):
        return self.title
