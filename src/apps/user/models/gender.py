from django.db import models


class Gender(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    
    ALL_GENDERS = [MALE, FEMALE]
    
    name = models.CharField(max_length=6)
    
    class Meta:
        db_table = 'genders'
