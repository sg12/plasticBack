from django.urls import path, include
from .views import *
from .routers import *


urlpatterns = [
    path('surgeons/', include(surgeon_router.urls)),
]
