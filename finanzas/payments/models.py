from django.db import models

from django.db.models.signals import pre_save

from django.utils.translation import gettext_lazy as _

from credits.models import Credit


class PaymentManager(models.Manager):
    
    def create_next_payment(self, credit, order, pay_day):
        return self.create(credit=credit, order=order, pay_day=pay_day)
    

class Payment(models.Model):
    
    class STATE(models.IntegerChoices):
        PENDING = 0, _('Pendiente')
        PAYED = 1, _('Pagado')
        FAILED = 2, _('Fallido')


    credit = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name='payments', null=True, blank=True)
    uuid = models.CharField(max_length=50, null=False, blank=False)
    order = models.IntegerField()
    amount = models.IntegerField(default=0, null=False, blank=False)
    pay_day = models.DateField(null=True, blank=True, default=None) # Día en el que se debe pagar
    payed_day = models.DateField(null=True, blank=True, default=None) # Día en el se pago
    state = models.IntegerField(default=STATE.PENDING, choices=STATE.choices) # PENDING
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = PaymentManager()
    
    def __str__(self):
        return f'{self.uuid}'
    

    @property
    def state_format(self):
        return Payment.STATE.choices[self.state][1]

    
def set_uuid(sender, instance, *args, **kwargs):
    if not instance.uuid:
        instance.uuid = str(uuid.uuid4())[:8]
        

pre_save.connect(set_uuid, sender=Credit)