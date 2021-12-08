from enum import Enum
from django.db import models
    
class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    curp = models.CharField(max_length=18, null=False, blank=False)
    DNI = models.CharField(max_length=50, null=False, blank=False) 
    marital_status = models.CharField(max_length=200, null=False, blank=False) # ENUM # relationship status
    spouse = models.CharField(max_length=200, null=False, blank=False) # Conyugue
    job = models.CharField(max_length=200, null=False, blank=False)
    children = models.IntegerField(null=False, blank=False, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} {self.last_name}'