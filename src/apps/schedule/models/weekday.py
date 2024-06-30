from django.db import models


class Weekday(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'weekdays'
        
    def __str__(self) -> str:
        return self.name
