from django.core.management.base import BaseCommand
from apps.user.models import Role


class Command(BaseCommand):
    help = "Init default models in a database"

    def handle(self, *args, **options):
        self.create_roles()
        self.stdout.write(self.style.SUCCESS('Init done'))
        
    def create_roles(self):
        for role_name in Role.get_list_roles():
            if not Role.objects.filter(name=role_name).exists():
                Role(name=role_name).save()
                self.stdout.write(self.style.SUCCESS(f'Create role: {role_name}'))
