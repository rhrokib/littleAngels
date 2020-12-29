from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import os
from django.utils import timezone

# Create your models here.

class AdoptionPost(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField();
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
    contact = models.CharField(max_length=11)
    isAdopted = models.BooleanField(default=False)
    image = models.ImageField( blank=True, null=True, upload_to= 'adoption_pics')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('adoption_post_detail', kwargs={'pk': self.pk})