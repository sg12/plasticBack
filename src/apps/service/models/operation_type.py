from django.db import models
from autoslug import AutoSlugField


class OperationType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    
    class Meta:
        db_table = 'operation_types'
    
    def __str__(self) -> str:
        return self.name
