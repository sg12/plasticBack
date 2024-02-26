from django.db import models


class Article(models.Model):
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'articles'