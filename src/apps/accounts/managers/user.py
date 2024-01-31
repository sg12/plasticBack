from django.contrib.auth.models import UserManager
from django.db.models import Avg, Count, IntegerField, FloatField
from django.db.models.functions import Coalesce


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
        
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.annotate(
            rating=Coalesce(
                Avg('reviews_about_me__rating'),
                0,
                output_field=FloatField()
            )
        )

        queryset = queryset.annotate(
            reviews_count=Coalesce(
                Count('reviews_about_me'),
                0,
                output_field=IntegerField()
            )
        )

        return queryset