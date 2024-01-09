from django.db import models


class Service(models.Model):
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE, related_name='services')
    service = models.ForeignKey('services.Service', on_delete=models.PROTECT, related_name='clinic_services')
    price = models.FloatField()

    class Meta:
        db_table = 'clinic_services'
