from django.contrib import admin
from .models import User, Review

admin.site.register((User, Review))
