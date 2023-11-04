from rest_framework import viewsets, permissions
from django.http import Http404
from .models import Post
from .serializer import PostSerializer
from rest_framework.renderers import JSONRenderer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'detele']:
            return [permissions.IsAdminUser()]
        
        return super().get_permissions()