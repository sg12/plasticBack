from django.core.management.base import BaseCommand
from apps.user.models import User, Role


class Command(BaseCommand):
    help = "Init default admin\nEmail: admin@gmail.com\nPassword: root"

    def handle(self, *args, **options):
        self.create_admin()

    def create_admin(self):
        username = 'Main Admin'
        email = 'admin@gmail.com'
        password = 'root'

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email, 
                password, 
                username=username, 
                role_name=Role.ADMIN
            )
            self.stdout.write(self.style.SUCCESS('Admin was created!\nEmail: admin@gmail.com\nPassword: root'))
        else:
            self.stdout.write(self.style.ERROR('Superuser already exists'))
