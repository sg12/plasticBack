from django.contrib import admin
from apps.support.models import Ticket, Message

admin.site.register([Ticket, Message])
