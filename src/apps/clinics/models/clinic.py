from django.db import models


class Clinic(models.Model):
    TYPE_OF_APPOINTMENT = [
        ("ONLINE", "Online"),
        ("CLINIC", "Clinic")
    ]
    
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    image = models.ImageField()
    metro = models.ManyToManyField('Metro', related_name='clinics')
    services = models.ManyToManyField('services.Service', related_name='clinics')
    type = models.CharField(max_length=20, choices=TYPE_OF_APPOINTMENT, default="ONLINE")
    price = models.FloatField()
    phone = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)
    # surgeons
    # work_times
     
    class Meta:
        db_table = 'clinics'