from django.contrib import admin
from apps.client.models import Client, QRCode


admin.site.register([Client, QRCode])
