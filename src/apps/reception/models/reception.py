from django.db import models


class Reception(models.Model):
    service = models.ForeignKey('service.Service', on_delete=models.CASCADE)
    client = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='receptions')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    status = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'receptions'
        
    def __str__(self) -> str:
        return f'{self.user.client.fio} - {self.service}'
