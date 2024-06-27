from pkg.mixins import *
from rest_framework.serializers import BaseSerializer
from rest_framework.mixins import DestroyModelMixin
from rest_framework.generics import GenericAPIView


class LCUD_APIView(
        BaseModelMixin,
        ListModelMixin,
        CreateModelMixin,
        UpdateModelMixin,
        DestroyModelMixin, 
        GenericAPIView
    ):

    create_serializer: BaseSerializer
    update_serializer: BaseSerializer
    
    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return self.result_class
            case 'POST':
                return self.create_serializer
            case 'PUT' | 'PATCH':
                return self.update_serializer
            
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
