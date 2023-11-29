from rest_framework.routers import DefaultRouter
from .views import SurgeonView

surgeon_router = DefaultRouter()
surgeon_router.register('', SurgeonView)