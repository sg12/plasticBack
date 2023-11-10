from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    image = models.ImageField()
    metro = models.ManyToManyField('Metro')
    services = models.ManyToManyField('Service')
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    price = models.FloatField()
    phone = models.CharField(max_length=20)
    work_time = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'clinics'
        
    def __str__(self) -> str:
        return self.name