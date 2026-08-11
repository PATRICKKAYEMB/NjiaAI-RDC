from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    choices = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=50, choices=choices, default='user')

    def __str__(self) -> str:
        return self.username

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    saved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    is_user = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        sender = "User" if self.is_user else "AI"
        return f"{sender}: {self.content[:20]}..."

class DocumentMetadata(models.Model):
    
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name