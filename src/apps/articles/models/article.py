from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='articles')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    class Meta:
        db_table = 'articles'