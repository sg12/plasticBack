from django.db import models


class Employe(models.Model):
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'clinic_employes'
    
    def __str__(self) -> str:
        return f'{self.doctor.user.username} ({self.clinic.name})'
