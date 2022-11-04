from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    biography = models.TextField(blank=True, null=True)
    twitter = models.CharField(max_length=140, blank=True, null=True)
    facebook = models.CharField(max_length=140, blank=True, null=True)
    instagram = models.CharField(max_length=140, blank=True, null=True)
    
    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'user'
        verbose_name_plural = 'users'