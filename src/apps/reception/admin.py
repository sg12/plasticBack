from django.contrib import admin
from apps.reception.models import Reception, ReceptionType

admin.site.register([Reception, ReceptionType])
