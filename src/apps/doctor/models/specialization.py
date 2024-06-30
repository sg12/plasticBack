from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=50)
    operation_type = models.ForeignKey('service.OperationType', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = 'doctor_specialications'
        
    def __str__(self) -> str:
        return self.name
