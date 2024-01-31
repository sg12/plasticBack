from django.db import models


class FAQ(models.Model):
    name = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    class Meta:
        db_table = 'faq'

    def __str__(self):
        return self.name
