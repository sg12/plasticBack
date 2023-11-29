from rest_framework.routers import DefaultRouter
from .views import ClinicView


clinic_router = DefaultRouter()
clinic_router.register('', ClinicView)