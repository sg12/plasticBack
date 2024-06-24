from django.contrib import admin
from apps.clinic.models import Clinic, Employe

admin.site.register([Clinic, Employe])
