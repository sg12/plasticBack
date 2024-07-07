from django.db import models


class Service(models.Model):
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE, related_name='services', null=True)
    specialty = models.ForeignKey('Specialty', on_delete=models.PROTECT, null=True)
    price = models.FloatField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'services'

    def __str__(self) -> str:
        return f'{self.doctor.user.email} - {self.specialty.name} ({self.price})'
