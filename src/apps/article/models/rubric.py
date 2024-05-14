from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=50)
    
    # articles
    
    class Meta:
        db_table = 'articles_rubrics'
        
    def __str__(self) -> str:
        return self.name
