from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def _create_user(self, login: str, email: str, password: str, **extra_fields):
        if not login or not email:
            raise ValueError("Login or email is empty")
        
        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **extra_fields)
        
        user.set_password(password)
        user.save()
        
    def create_user(self, login: str, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        self._create_user(login, email, password, **extra_fields)
        
    def create_superuser(self, login: str, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        self._create_user(login, email, password, **extra_fields)
        
    