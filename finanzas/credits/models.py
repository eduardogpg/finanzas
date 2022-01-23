import uuid
from enum import IntEnum

from django.db import models
from prospects.models import Client

from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

from users.models import User

from groups.models import Group
from folders.models import Folder

class Credit(models.Model):
    
    class STATE(models.IntegerChoices):
        CREATED = 0, _('Creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')

    
    class CYCLE(models.IntegerChoices):
        WEEKLY = 0, _('Semanal')
 
     
    class VISIT_DAY(models.IntegerChoices):
        MONDAY = 0, _('Lunes')
        TUESDAY = 1, _('Martes')
        WEDNESDAY = 2, _('Miércoles')
        THURSDAY = 3, _('Jueves')
        FRIDAY = 4, _('Viernes')
        SATURDAY = 5, _('Sábado')
        SUNDAY = 6, _('Domingo')


    class VISIT_TIME(models.IntegerChoices):
        NINE = 9, _('9:00 AM')
        TEN = 10, _('10:00 AM')
        ELEVEN = 11, _('11:00 AM')
        TWELVE = 12, _('12:00 PM')
        THIRTEEN = 13, _('13:00 PM') 
        FOURTEEN = 14, _('14:00 PM')
        FIFTEEN = 15, _('15:00 PM')
        SIXTEEN = 16, _('16:00 PM')
        SEVENTEEN = 17, _('17:00 PM')
        EIGHTTEEN = 18, _('18:00 PM')
        NINETEEN = 19, _('19:00 PM')
        TWENTY = 29, _('20:00 PM')
        
    
    uuid = models.CharField(max_length=50, null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='credits', null=True, blank=True)
    
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='credits', null=True, blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='credits', null=True, blank=True)
    
    request_amount = models.IntegerField(default=0, null=False, blank=False) #Cents?
    authorized_amount = models.IntegerField(default=0, null=False, blank=False) #Cents?
    state = models.IntegerField(default=STATE.CREATED, choices=STATE.choices) # CREATED
    
    cycle = models.IntegerField(default=0, choices=CYCLE.choices) # Semanal
    
    term = models.IntegerField(default=0, null=False, blank=False)
    visit_day = models.IntegerField(default=0, choices=VISIT_DAY.choices, null=False, blank=False) # Día de la visita
    visit_time = models.IntegerField(default=0, choices=VISIT_TIME.choices, null=False, blank=False) # Hola de la visita
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.uuid}'
    
    @property
    def visit_day_format(self):
        return Credit.VISIT_DAY.choices[self.visit_day][1]
    

    @property
    def visit_time_format(self):
        for val, text in Credit.VISIT_TIME.choices:
            if val == self.visit_time:
                return text
    
        return ''
    
    
def set_uuid(sender, instance, *args, **kwargs):
    if not instance.uuid:
        instance.uuid = str(uuid.uuid4())[:8]


pre_save.connect(set_uuid, sender=Credit)