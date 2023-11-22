from django.db import models


class SurgeonService(models.Model):
    surgeon = models.ForeignKey('Surgeon', on_delete=models.CASCADE, related_name='surgeon_services')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    
    class Meta:
        db_table = 'surgeon_services'
    
    def __str__(self) -> str:
        return self.name