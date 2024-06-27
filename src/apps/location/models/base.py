from django.db import models
from autoslug import AutoSlugField


class BaseLocation(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True
