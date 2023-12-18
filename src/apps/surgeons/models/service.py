from django.db import models


class Service(models.Model):
    surgeon = models.ForeignKey('Surgeon', on_delete=models.CASCADE, related_name='services')
    service = models.ForeignKey('services.Service', on_delete=models.PROTECT, related_name='surgeon_services')
    price = models.FloatField()
    
    class Meta:
        db_table = 'surgeon_services'