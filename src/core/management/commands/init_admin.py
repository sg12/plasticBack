from django.core.management.base import BaseCommand
from apps.accounts.models import User


class Command(BaseCommand):
    help = "Create admin user"

    def handle(self, *args, **options):
        email = 'admin@admin.com'
        password = 'root'

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email, password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))