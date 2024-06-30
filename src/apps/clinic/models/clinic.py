from django.db import models
from apps.clinic.managers import ClinicManager


class Clinic(models.Model):    
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='clinic')
    official_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    
    metro = models.ForeignKey('location.Metro', on_delete=models.PROTECT, related_name='clinics', null=True, blank=True)
    district = models.ForeignKey('location.District', on_delete=models.PROTECT, related_name='clinics', null=True, blank=True)
    city = models.ForeignKey('location.City', on_delete=models.PROTECT, related_name='clinics', null=True, blank=True)

    objects = ClinicManager()
    
    # employes
    # worktimes
    # ratings
    # reviews

    class Meta:
        db_table = 'clinics'

    def __str__(self) -> str:
        return f'{self.user.email}'
