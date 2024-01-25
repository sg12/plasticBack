from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def _create_user(self, email: str, password: str, **extra_fields):
        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save()
        
    def create_user(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        self._create_user(email, password, **extra_fields)
        
    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        self._create_user(email, password, **extra_fields)
        
    