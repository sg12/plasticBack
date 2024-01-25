from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls


api_v1 = [
    path('', include('apps.clients.urls')),
    path('', include('apps.surgeons.urls')),
    path('', include('apps.clinics.urls')),
    path('', include('apps.services.urls')),
    path('', include('apps.articles.urls')),
    path('', include('apps.authentication.urls')),
    path('', include('apps.accounts.urls')),
    path('', include('apps.faq.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("__debug__/", include("debug_toolbar.urls")),
    path('api/v1/', include(api_v1)),
]

urlpatterns += doc_urls
