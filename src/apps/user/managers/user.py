from django.contrib.auth.models import UserManager
from django.db.models import Avg, Count, IntegerField, FloatField
from django.db.models.functions import Coalesce
from django.apps import apps


class CustomUserManager(UserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        Role = apps.get_model('user', 'Role')
        
        role_name = extra_fields.pop('role_name')
        role = Role.objects.get(name=role_name)
        extra_fields.setdefault('role', role)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        self.create_role_model(user, role_name)

        return user
        
    def create_superuser(self, email, password, **extra_fields):
        Role = apps.get_model('user', 'Role')
        
        extra_fields.setdefault('role_name', Role.ADMIN)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
    
    def create_role_model(self, user, role_name):
        Role = apps.get_model('user', 'Role')
        Client = apps.get_model('client', 'Client')
        Doctor = apps.get_model('doctor', 'Doctor')
        Clinic = apps.get_model('clinic', 'Clinic')
        
        model = None
        match role_name:
            case Role.CLIENT:
                model = Client
            case Role.DOCTOR:
                model = Doctor
            case Role.CLINIC:
                model = Clinic
            case Role.ADMIN:
                return
        
        if model:
            return model(user=user).save()
        
        raise ValueError('wrong role')
    
    
    # TODO реализовать создание QRCode
    def create_qrcode(self):
        pass
        
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.annotate(
            rating=Coalesce(
                Avg('reviews__rating'),
                0,
                output_field=FloatField()
            )
        )

        queryset = queryset.annotate(
            reviews_count=Coalesce(
                Count('reviews'),
                0,
                output_field=IntegerField()
            )
        )

        return queryset
