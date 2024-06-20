from django.db import models


class ReceptionType(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'reception_types'
    
    def __str__(self) -> str:
        return self.name
    
