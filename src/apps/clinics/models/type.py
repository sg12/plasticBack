from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'service_types'
        
    def __str__(self) -> str:
        return self.name  