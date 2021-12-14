from datetime import datetime
from django.db import models

from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    permission_level = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    
    objects = UserManager()

    def authenticate_now(self):
        self.last_login_at = datetime.now()
        self.save()