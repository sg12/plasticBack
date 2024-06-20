from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'doctor_specialties'
        
    def __str__(self) -> str:
        return self.name
