from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from apps.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDERS = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
    )

    email = models.EmailField(max_length=50, unique=True)
    password = models.TextField()
    type = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    username = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDERS, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'