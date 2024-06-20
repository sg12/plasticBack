from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tickets'
        
    def __str__(self) -> str:
        return self.title
