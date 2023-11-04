from rest_framework import routers
from .views import PostsViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)