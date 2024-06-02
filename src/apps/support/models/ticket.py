from django.db import models


class Ticket(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    theme = models.CharField(max_length=150)
    description = models.TextField()
    url = models.URLField()
    details = models.TextField()
    file = models.FileField(upload_to='support/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tickets'
        
    def __str__(self) -> str:
        return self.theme
