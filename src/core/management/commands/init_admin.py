from django.core.management.base import BaseCommand
from apps.user.models import User, Role


class Command(BaseCommand):
    help = "Create admin user"

    def handle(self, *args, **options):
        username = 'Main Admin'
        email = 'admin@gmail.com'
        password = 'root'

        Role.objects.init_roles()

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email, password, username=username)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.ERROR('Superuser already exists'))
