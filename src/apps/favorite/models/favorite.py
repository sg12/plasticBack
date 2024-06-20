from django.db import models


class Favorite(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'favorites'
        
    def __str__(self) -> str:
        return f'{self.author.email} saved {self.account.email}'
