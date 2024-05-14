from rest_framework import serializers
from apps.doctor.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()
