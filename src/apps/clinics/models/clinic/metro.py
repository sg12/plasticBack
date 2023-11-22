from django.db import models


class Metro(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'metro'
        
    def __str__(self) -> str:
        return self.name