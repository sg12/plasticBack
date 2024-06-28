from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from apps.user.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):    
    email = models.EmailField(max_length=50, unique=True)
    password = models.TextField()
    
    username = models.CharField(max_length=50, null=True, blank=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices={
        'male': 'male',
        'female': 'female'
    }, max_length=6, blank=True, null=True)
    
    confidentiality_consent = models.BooleanField(default=False)
    personal_data_consent = models.BooleanField(default=False)
    review_consent = models.BooleanField(default=False)
    news_consent = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    # client
    # doctor
    # clinic
    # articles
    # services
    # schedules

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self) -> str:
        return self.email
