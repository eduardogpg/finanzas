from django.db import models

from folders.models import Folder

class Group(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='groups')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name