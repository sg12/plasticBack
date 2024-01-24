from django.db import models


class FAQ(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()

    class Meta:
        db_table = 'faq'

    def __str__(self):
        return self.name
