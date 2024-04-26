from django.db import models

class Statiy(models.Model):
    title = models.CharField(max_length=255)
    opisanie = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'statiy'

