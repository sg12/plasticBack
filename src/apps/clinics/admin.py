from django.contrib import admin
from .models import (
    Clinic,
    Metro,
    District,
    Service,
    Type
)


admin.site.register((Clinic, Metro, District, Service, Type))