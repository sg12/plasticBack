from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=7)
    slug = models.SlugField(max_length=6)
    
    class Meta:
        db_table = 'genders'
