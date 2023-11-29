from django.db import models

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDERS = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
    )
        
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20, choices=GENDERS, default='male')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # surgeon

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'