from django.db import models


class Reception(models.Model):
    service = models.ForeignKey('service.Service', on_delete=models.CASCADE)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, related_name='receptions')
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE, related_name='receptions')
    datetime = models.DateTimeField()
    status = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'receptions'
        
    def __str__(self) -> str:
        return f'{self.client.fio} - {self.service}'
