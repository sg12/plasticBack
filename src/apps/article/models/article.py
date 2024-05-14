from django.db import models


class Article(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short = models.TextField()
    description = models.TextField()
    rubric = models.ForeignKey('Rubric', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articles'

    def __str__(self) -> str:
        return self.title
