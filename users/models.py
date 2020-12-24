from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',  upload_to= 'profile_pics')
    
    def __str__(self):
        return self.user.username























    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)

    #     # Resizing the image to 300x300 px
    #     if img.height > 300 or img.width > 300:
    #         output = (300, 300)
    #         img.thumbnail(output)
    #         img.save(self.path)
