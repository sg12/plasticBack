from django.contrib import admin
from apps.service.models import *


admin.site.register([
    Service, 
    Specialty, 
    OperationType
])
