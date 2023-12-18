from django.db import models
from apps.surgeons.validators import workplace_validator


class Workplace(models.Model):
    surgeon = models.ForeignKey('Surgeon', on_delete=models.CASCADE, related_name='workplaces')
    place = models.CharField(max_length=255)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    post = models.CharField(max_length=50)

    class Meta:
        db_table = 'surgeon_workplace'