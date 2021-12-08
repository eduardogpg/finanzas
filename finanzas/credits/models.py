from enum import Enum

from django.db import models
from clients.models import Client

class CreditState(Enum):
    CREATED = 0
    AUTHORIZED = 1
    COMPLETED = 2

class Credit(models.Model):
    folder = models.CharField(max_length=100, null=False, blank=False)
    uuid = models.CharField(max_length=50, null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    request_amount = models.IntegerField(default=0, null=False, blank=False) #Cents?
    authorized_amount = models.IntegerField(default=0, null=False, blank=False) #Cents?
    state = models.IntegerField(default=0, choices=[(state, state.value) for state in CreditState] ) # CREATED
    cycle = models.IntegerField(default=0) # Semanal
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{uuid} - '