from django.db import models


class Reception(models.Model):
    service = models.ForeignKey('service.Service', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='receptions')
    datetime = models.DateTimeField()
    status = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'receptions'
        
    def __str__(self) -> str:
        return f'{self.user.email} -> {self.service}'
