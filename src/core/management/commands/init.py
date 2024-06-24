from django.core.management.base import BaseCommand
from apps.user.models import User, Role, Gender


class Command(BaseCommand):
    help = "Init models in a database"

    def handle(self, *args, **options):
        self.create_roles()
        self.create_genders()
        self.create_admin()
        self.stdout.write(self.style.SUCCESS('Init done'))
        
    def create_roles(self):
        for role_name in Role.ALL_ROLES:
            if not Role.objects.filter(name=role_name).exists():
                Role(name=role_name).save()
                self.stdout.write(self.style.SUCCESS(f'Create role: {role_name}'))
                
    def create_genders(self):
        for gender_name in Gender.ALL_GENDERS:
            if not Gender.objects.filter(name=gender_name).exists():
                Gender(name=gender_name).save()
                self.stdout.write(self.style.SUCCESS(f'Create gender: {gender_name}'))
            
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
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.ERROR('Superuser already exists'))
