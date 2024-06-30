from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'doctors_categories'
    
    def __str__(self) -> str:
        return self.name
