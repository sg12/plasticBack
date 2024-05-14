from django.db import models
from django.utils.text import slugify


class BaseLocation(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True
