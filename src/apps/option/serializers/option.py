from rest_framework import serializers
from apps.option.models import Option


class OptionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    
    class Meta:
        model = Option
        exclude = ('category',)
