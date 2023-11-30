from django.contrib import admin
from django.urls import path, include


api_v1 = [
    path('', include('apps.clinics.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.surgeons.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/v1/', include(api_v1))
]
