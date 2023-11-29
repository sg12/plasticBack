from django.db import models


class Specialtie(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'surgeon_specialties'