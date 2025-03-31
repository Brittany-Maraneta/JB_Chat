from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User)


    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)  # Use ForeignKey to User model
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content}'


class Avatar(models.Model):
    name = models.CharField(max_length=100)
    file_location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    avatar = models.ManyToManyField(Avatar)

    def __str__(self):
        return f"{self.user.username}'s Profile"