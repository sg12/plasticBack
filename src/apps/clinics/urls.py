from django.urls import path, include
from .views import *
from .routers import *


urlpatterns = [
    path('clinics/', include(clinic_router.urls)),
    path('surgeon/', include(surgeon_router.urls)),
    path('metro/', MetroListView.as_view()),
    path('district/', DistrictListView.as_view()),
]
