from django.db import models
from django.utils.text import slugify


class Specialization(models.Model):
    name = models.CharField(max_length=50)
    operation_type = models.ForeignKey('OperationType', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'services_info'
        
    def __str__(self) -> str:
        return self.name
