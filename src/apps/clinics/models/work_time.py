from django.db import models


class WorkTime(models.Model):
    WEEKDAY = (
        ('MON', 'monday'),
        ('TUE', 'tuesday'),
        ('WED', 'wednessday'),
        ('THU', 'thursday'),
        ('FRI', 'friday'),
        ('SAT', 'saturday'),
        ('SUN', 'sunday')
    )
    
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE, related_name='work_times')
    weekday = models.CharField(max_length=20, choices=WEEKDAY)
    start = models.TimeField()
    end = models.TimeField()
    
    class Meta:
        db_table = 'clinic_work_times'