from django.db import models
from django.utils.text import slugify


class OperationType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'operation_types'
    
    def __str__(self) -> str:
        return self.name
