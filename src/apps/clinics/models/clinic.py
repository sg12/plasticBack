from django.db import models
from apps.clinics.managers import ClinicManager


class Clinic(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='clinic')
    director = models.CharField(max_length=50, null=True, blank=True)
    metro = models.ManyToManyField('Metro', related_name='clinics', blank=True)
    open_time = models.TimeField(null=True, blank=True)  # открыто с 9:00
    close_time = models.TimeField(null=True, blank=True)  # открыто до 21:00
    description = models.TextField(null=True, blank=True)
    specialization = models.TextField(null=True, blank=True)

    objects = ClinicManager()

    # worktimes
    # services
    # ratings
    # reviews

    class Meta:
        db_table = 'clinics'
