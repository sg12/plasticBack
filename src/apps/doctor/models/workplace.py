from django.db import models


class Workplace(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='workplaces')
    organization = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    post = models.CharField(max_length=255)

    class Meta:
        db_table = 'doctor_workplaces'
        
    def __str__(self) -> str:
        return f'{self.doctor.fio}: {self.organization}'
