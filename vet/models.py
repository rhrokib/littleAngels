from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import os
from django.utils import timezone


class Vet(models.Model):

    vet_name = models.CharField(max_length=30, default='Vet')
    institute = models.CharField(max_length=30)
    certification = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    work_hours = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='vet_pics')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse('vet_post_detail', kwargs={'pk': self.pk})
