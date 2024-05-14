from django.db import models


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    time = models.TimeField()
    
    class Meta:
        db_table = 'doctor_schedules'
        unique_together = ('date', 'time')
        
    def __str__(self) -> str:
        return f'{self.user.email}: {self.weekday} {self.time}'
