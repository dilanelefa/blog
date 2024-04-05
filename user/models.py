from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='profile_pics', blank=True)
    last_name = None
    first_name = None

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
