from django.contrib import admin
from apps.location.models import City, District, Metro

admin.site.register([City, District, Metro])
