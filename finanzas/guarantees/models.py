from django.db import models

from prospects.models import Client

class Guarantee(models.Model):
    description = models.TextField(null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='guarantees')
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Garantia Cliente N° {self.client_id}'
