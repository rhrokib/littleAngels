from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import os
from django.utils import timezone

class Shop(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField();
    location = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=11, default='', blank=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE); #if user is deleted, all post gets deleted
    image = models.ImageField( null=True, upload_to= 'food_pics')
    price = models.IntegerField()

    def __str__(self):
        return self.title

        
    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'pk': self.pk})
