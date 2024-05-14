from django.contrib import admin
from .models import User, Role, Gender

admin.site.register([
    User, 
    Role, 
    Gender
])
