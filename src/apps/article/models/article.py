from django.db import models


class Article(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rubric = models.ForeignKey('article.Rubrics', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='article/', null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'articles'