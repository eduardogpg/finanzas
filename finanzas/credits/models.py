import uuid
from enum import IntEnum

from django.db import models
from prospects.models import Client

from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _


class Credit(models.Model):
    
    class STATE(models.IntegerChoices):
        CREATED = 0, _('Creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')

    
    class CYCLE(models.IntegerChoices):
        WEEKLY = 0, _('Semanal')
 
    
    folder = models.CharField(max_length=100, null=False, blank=False, default='Finanzas del sur')
    uuid = models.CharField(max_length=50, null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    request_amount = models.IntegerField(default=0, null=False, blank=False) #Cents?
    authorized_amount = models.IntegerField(default=0, null=False, blank=False) #Cents?
    state = models.IntegerField(default=STATE.CREATED, choices=STATE.choices) # CREATED
    cycle = models.IntegerField(default=0, choices=CYCLE.choices) # Semanal
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.uuid}'
    

def set_uuid(sender, instance, *args, **kwargs):
    if not instance.uuid:
        instance.uuid = str(uuid.uuid4())[:8]


pre_save.connect(set_uuid, sender=Credit)