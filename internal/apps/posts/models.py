from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField()
    description = models.TextField()
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name="posts")
    
    def __str__(self) -> str:
        return self.title