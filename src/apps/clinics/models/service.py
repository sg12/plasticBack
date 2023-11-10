from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'services'
        
    def __str__(self) -> str:
        return self.name  