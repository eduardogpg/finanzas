from enum import IntEnum

from django.db import models
from prospects.models import Client

from django.utils.translation import gettext_lazy as _

class Credit(models.Model):
    
    class Status(models.IntegerChoices):
        CREATED = 0, _('Creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    folder = models.CharField(max_length=100, null=False, blank=False)
    uuid = models.CharField(max_length=50, null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    request_amount = models.IntegerField(default=0, null=False, blank=False) #Cents?
    authorized_amount = models.IntegerField(default=0, null=False, blank=False) #Cents?
    state = models.IntegerField(default=Status.CREATED, choices=Status.choices) # CREATED
    cycle = models.IntegerField(default=0) # Semanal
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.uuid}'
    
