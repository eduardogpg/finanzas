from django.db import models

from django.db.models.signals import pre_save

from django.utils.translation import gettext_lazy as _

from credits.models import Credit


class PaymentManager(models.Manager):
    
    def create_next_payment(self, credit, order, pay_day):
        return self.create(credit=credit, order=order, pay_day=pay_day)
    

class Payment(models.Model):
    
    class STATE(models.IntegerChoices):
        CREATED = 0, _('Creado')
        PAYED = 1, _('Pagado')
        FAILED = 2, _('Fallido')


    credit = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name='payments', null=True, blank=True)
    uuid = models.CharField(max_length=50, null=False, blank=False)
    order = models.IntegerField()
    pay_day = models.DateField(null=True, blank=True, default=None)
    state = models.IntegerField(default=STATE.CREATED, choices=STATE.choices) # CREATED
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = PaymentManager()
    
    def __str__(self):
        return f'{self.uuid}'
    

    
def set_uuid(sender, instance, *args, **kwargs):
    if not instance.uuid:
        instance.uuid = str(uuid.uuid4())[:8]
        

pre_save.connect(set_uuid, sender=Credit)