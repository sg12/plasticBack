from django.db import models


class Favorite(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='author_favorites')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='user_favorites')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'favorites'
        
    def __str__(self) -> str:
        return f'{self.author.email} saved {self.user.email}'
