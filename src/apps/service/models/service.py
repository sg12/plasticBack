from django.db import models


class Service(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='services')
    specialty = models.ForeignKey('Specialty', on_delete=models.PROTECT, null=True)
    price = models.FloatField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'services'

    def __str__(self) -> str:
        return f'{self.user.email} - {self.specialization.name} ({self.price})'
