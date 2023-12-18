from django.db import models


class Specialtie(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        db_table = 'surgeon_specialties'