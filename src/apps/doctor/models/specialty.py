from django.db import models
from django.utils.text import slugify


class Specialty(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'doctor_specialties'
        
    def __str__(self) -> str:
        return self.name
