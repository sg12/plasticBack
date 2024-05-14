from django.db import models


class Degree(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'doctor_degrees'
    
    def __str__(self) -> str:
        return self.name
