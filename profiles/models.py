from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...")
    avatar = models.ImageField(upload_to='avatars', default='157-1579943_no-profile-picture-round')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
    