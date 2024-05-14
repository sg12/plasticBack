from django.db import models


class Qualification(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='qualifications')
    retraining = models.CharField(max_length=255)
    date = models.DateField()
    
    class Meta:
        db_table = 'doctor_qualifications'
    
    def __str__(self) -> str:
        return f' {self.doctor.fio}: {self.retraining}'
