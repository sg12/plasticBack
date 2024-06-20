from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=7)
    
    class Meta:
        db_table = 'genders'
