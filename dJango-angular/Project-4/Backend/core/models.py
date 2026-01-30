from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=225)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []