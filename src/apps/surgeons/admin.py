from django.contrib import admin
from .models import *


admin.site.register((
    Education,
    Workplace,
    Surgeon,
    Specialtie
))
