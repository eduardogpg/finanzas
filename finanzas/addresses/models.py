from django.db import models

from prospects.models import Prospect

class Address(models.Model):
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False, blank=False)
    zip = models.IntegerField(null=False, blank=False)
    state = models.IntegerField(default=0, null=False, blank=False) # Chiapas
    suburb = models.CharField(max_length=255, null=False, blank=False) # Colonia
    township = models.CharField(max_length=255, null=False, blank=False) # Ciudad
    lat = models.IntegerField(null=True)
    long = models.IntegerField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'#{self.address} - {self.township}'
    
    