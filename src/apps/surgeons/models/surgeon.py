from django.db import models
from apps.surgeons.managers import SurgeonManager


class Surgeon(models.Model):
    RECEPTION = (
        ('private', 'private'),
        ('clinic', 'clinic'),
    )

    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='surgeon')
    site = models.URLField(null=True, blank=True)
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.SET_NULL, related_name='surgeons', null=True, blank=True)
    specialtie = models.ForeignKey('Specialtie', on_delete=models.PROTECT, related_name='surgeons', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    experience = models.PositiveSmallIntegerField(null=True, blank=True)  # стаж
    category = models.PositiveSmallIntegerField(null=True, blank=True)
    academic = models.PositiveSmallIntegerField(null=True, blank=True)  # ученая степень
    reception = models.CharField(max_length=20, choices=RECEPTION, default=RECEPTION[0][0])

    objects = SurgeonManager()

    # educations
    # workplaces
    # services
    # reviews
    # ratings

    class Meta:
        db_table = 'surgeons'
