from django.contrib import admin
from apps.option.models import Option, OptionCategory

admin.site.register([Option, OptionCategory])
