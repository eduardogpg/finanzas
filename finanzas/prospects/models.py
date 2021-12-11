from django.db import models

class Prospect(models.Model):
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
    
    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'
    
    
class Client(models.Model):
    prospect = models.OneToOneField(
        Prospect, on_delete=models.CASCADE, primary_key=True,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.prospect.full_name}'
    

class Aval(models.Model):
    prospect = models.OneToOneField(
        Prospect, on_delete=models.CASCADE, primary_key=True,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.prospect.full_name}'
    

class Reference(models.Model):
    prospect = models.OneToOneField(
        Prospect, on_delete=models.CASCADE, primary_key=True,
    )
    
    relationship = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.prospect.full_name}'
