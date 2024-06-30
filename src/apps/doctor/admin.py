from django.contrib import admin
from .models import *


admin.site.register((
    Education,
    Workplace,
    Doctor,
    Specialization,
    Category,
    Degree,
    Qualification
))
