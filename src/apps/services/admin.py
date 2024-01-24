from django.contrib import admin
from .models import Service, ServiceInfo

admin.site.register((Service, ServiceInfo))