from django.db import models


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        db_table = 'faq'

    def __str__(self):
        return self.name
