from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)
    full_name = models.CharField(max_length=150, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices = [
            ('male','Male'),
            ('female','Female'),
            ('other','Other'),
        ],
        blank=True
    )
    contact_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.full_name or self.email
    
