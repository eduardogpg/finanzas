from django.db import models

from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    permission_level = models.IntegerField(default=0)
    objects = UserManager()
