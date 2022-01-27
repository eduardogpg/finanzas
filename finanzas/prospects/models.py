from django.db import models

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _


class Prospect(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    curp = models.CharField(max_length=18, null=True, blank=True)
    DNI = models.CharField(max_length=50, null=True, blank=True) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.name} {self.last_name}'
    
    
    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'


    @property
    def address(self):
        return self.addresses.first()


class Client(models.Model):
    
    class MARITAL_STATE_CHOICES(models.IntegerChoices):
        SINGLE = 0, _('Soltero(a)')
        MARRIED = 1, _('Casado(a)')
        DIVORCED = 2, _('Divorciado(a)')
        ENGAGGED = 3, _('Comprometido(a)')
        SINGLE_FATHER = 4, _('Padre Soltero(a)')
        WINDOWER = 5, _('Viudo(a)')
        FREE_UNION = 6, _('Unión Libre)')


    marital_state = models.IntegerField(choices=MARITAL_STATE_CHOICES.choices, default=0, null=False, blank=False) # ENUM # relationship status
    spouse = models.CharField(max_length=200, null=False, blank=False) # Conyugue
    job = models.CharField(max_length=200, null=False, blank=False)
    children = models.IntegerField(null=False, blank=False, default=0)
    prospect = models.OneToOneField(Prospect, on_delete=models.CASCADE, primary_key=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.prospect.full_name}'
    
    
    @property
    def address(self):
        return self.prospect.addresses.first()
    

    @property
    def aval(self):
        return self.avals.first()
    
    
    @property
    def full_name(self):
        return f'{self.prospect.name} {self.prospect.last_name}'
    

    @property
    def marital_state_format(self):
        return Client.MARITAL_STATE_CHOICES.choices[self.marital_state][1]
    
    
    
    @property
    def credit(self):
        return self.credits.first()
    
    
    @property
    def lat(self):
        # return self.prospect.address.lat    
        return 16.781174
    
    
    @property
    def long(self):
        # return self.prospect.address.long
        return -93.098344
    
    
class Aval(models.Model):
    prospect = models.OneToOneField(Prospect, on_delete=models.CASCADE, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='avals')
    
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.prospect.full_name}'
    
    
class ReferenceManager(models.Manager):
    
    def create_reference(self, client, data):
        from addresses.models import Address
        
        prospect = Prospect.objects.create(name=data['name'])
        address = Address.objects.create(address=data['address'], prospect=prospect)
        
        return self.create(
            client=client,
            prospect=prospect,
            relationship=data['relationship'],
            contact=data['contact']
        )
        

class Reference(models.Model):
    prospect = models.OneToOneField(Prospect, on_delete=models.CASCADE, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='references')
    
    relationship = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = ReferenceManager()
    
    
    def __str__(self):
        return f'{self.prospect.full_name}'

