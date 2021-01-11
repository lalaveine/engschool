from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars')
    bio = models.CharField(max_length=200)
    twitter_link = models.CharField(max_length=200, default="#")
    fb_link = models.CharField(max_length=200, default="#")
    instagram_link = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.user.username
