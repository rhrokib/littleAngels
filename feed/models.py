from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import os
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField();
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE); #if user is deleted, all post gets deleted
    approved = models.BooleanField(default=False)
    image = models.ImageField( blank=True, null=True, upload_to= 'happy_pics')

    def __str__(self):
        return self.title

        
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})



