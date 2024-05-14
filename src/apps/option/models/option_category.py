from django.db import models


class OptionCategory(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'option_categories'

    def __str__(self) -> str:
        return self.name
