from django.db import models
from apps.user.managers import RoleManager
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    CLIENT = 'CLIENT'
    DOCTOR = 'DOCTOR'
    CLINIC = 'CLINIC'
    ADMIN = 'ADMIN'
    
    DEFAULT_ROLES = (
        (CLIENT, _(CLIENT)),
        (DOCTOR, _(DOCTOR)),
        (CLINIC, _(CLINIC))
    )
    
    name = models.CharField(max_length=10, choices=DEFAULT_ROLES)
    
    objects = RoleManager()
    
    def __str__(self) -> str:
        return self.name
