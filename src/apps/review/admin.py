from django.contrib import admin
from .models import Review, Reply

admin.site.register([Review, Reply])
