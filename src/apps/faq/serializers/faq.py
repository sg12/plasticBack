from rest_framework import serializers
from apps.faq.models import FAQ


class FAQListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
