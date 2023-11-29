from django.db import models


class District(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'districts'