from rest_framework import serializers
from django.db.models import Model


class EntityFromURL:
    requires_context: bool = True
    name: str = None
    model: Model = None
    
    def __init__(self, name: str, model: Model):
        '''
        `name` - имя переменной в url\n
        `model` - модель для queryset
        '''
        
        self.name = name
        self.model = model

    def __call__(self, serializer_field):
        view = serializer_field.context['view']
        kwargs = view.kwargs
        pk = kwargs[self.name]
        
        queryset = self.model.objects.filter(pk=pk)
        
        field = serializers.PrimaryKeyRelatedField(queryset=queryset)
        field.run_validation(data=pk)
        
        return queryset.first()
