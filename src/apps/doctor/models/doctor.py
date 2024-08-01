from django.db import models
from apps.doctor.managers import DoctorManager


class Doctor(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='doctor')
    site = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    experience = models.PositiveSmallIntegerField(default=0, blank=True)
    
    clinic_user = models.ForeignKey('user.User', on_delete=models.SET_NULL, related_name='clinic_employes', blank=True, null=True)
    reception_types = models.ManyToManyField('reception.ReceptionType', blank=True)
    specialization = models.ForeignKey('service.Specialization', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    degree = models.ForeignKey('Degree', on_delete=models.SET_NULL, null=True, blank=True)

    objects = DoctorManager()

    # licenses
    # educations
    # qualifications
    # workplaces
    # services
    # reviews
    # ratings
    # receptions

    class Meta:
        db_table = 'doctors'
        
    def __str__(self) -> str:
        return self.user.email
