from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    CLIENT = 'client'
    DOCTOR = 'doctor'
    CLINIC = 'clinic'
    ADMIN = 'admin'
    
    DEFAULT_ROLES = (
        (CLIENT, _(CLIENT)),
        (DOCTOR, _(DOCTOR)),
        (CLINIC, _(CLINIC))
    )
    
    name = models.CharField(max_length=10, choices=DEFAULT_ROLES)
    
    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_list_roles(cls) -> list[str]:
        return [cls.CLIENT, cls.DOCTOR, cls.CLINIC, cls.ADMIN]
