from django.db import models


class ServiceInfo(models.Model):
    OPERATION_TYPE = [
        ("body", "body"),
        ("face", "face"),
        ("other", "other")
    ]
    
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=OPERATION_TYPE)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        db_table = 'services_info'
        
    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='services')
    service_info = models.ForeignKey('ServiceInfo', on_delete=models.PROTECT, related_name='users')
    price = models.FloatField()
    active = models.BooleanField(default=False)

    class Meta:
        db_table = 'services'

    def __str__(self) -> str:
        return f'{self.service_info.name} ({self.price})'
