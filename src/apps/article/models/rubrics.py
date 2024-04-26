from django.db import models

class Rubrics(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        db_table = 'rubric'