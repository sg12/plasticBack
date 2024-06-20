from django.db import models


class ClinicSchedule(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='schedules')
    weekday = models.ForeignKey('Weekday', on_delete=models.PROTECT)
    time_start = models.TimeField()
    time_end = models.TimeField()
    
    class Meta:
        db_table = 'clinic_schedules'
        unique_together = (
            'weekday', 
            'time_start', 
            'time_end'
        )
        
    def __str__(self) -> str:
        return f'{self.user.email}: {self.weekday} {self.time_start}-{self.time_end}'
