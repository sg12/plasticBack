from django.db import models


class Schedule(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    class Meta:
        db_table = 'schedules'
        unique_together = ('date', 'time')
        
    def __str__(self) -> str:
        return f'{self.user.email}: {self.weekday} {self.time}'
