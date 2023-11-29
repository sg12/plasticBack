from django.contrib import admin
from .models import *


admin.site.register((
    Education,
    WorkPlace,
    Review,
    Service,
    Surgeon,
    Specialtie,
    Rating
))