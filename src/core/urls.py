from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView


api = [
    path('', include('apps.client.urls')),
    path('', include('apps.doctor.urls')),
    path('', include('apps.clinic.urls')),
    path('', include('apps.license.urls')),
    path('', include('apps.service.urls')),
    path('', include('apps.article.urls')),
    path('', include('apps.authentication.urls')),
    path('', include('apps.location.urls')),
    path('', include('apps.reception.urls')),
    path('', include('apps.user.urls')),
    path('', include('apps.faq.urls')),
    path('', include('apps.review.urls')),
    path('', include('apps.favorite.urls')),
    path('', include('apps.support.urls'))
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),

    # Debug tool
    # path("__debug__/", include("debug_toolbar.urls")),

    # Swagger
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
