from django_filters import rest_framework as filters
from apps.surgeons.models import Surgeon
from apps.users.models import User
from django.db.models import Count
from .models import Surgeon


class SurgeonFilter(filters.FilterSet):
    experience = filters.NumberFilter(field_name='experience', lookup_expr='gte')
    category = filters.NumberFilter(field_name='category', lookup_expr='exact')
    academic = filters.NumberFilter(lookup_expr='exact')
    gender = filters.ChoiceFilter(choices=User.GENDERS)
    reception = filters.ChoiceFilter(choices=Surgeon.RECEPTION)
    reviews_count = filters.NumberFilter(method='get_reviews_count')
    
    class Meta:
        model = Surgeon
        fields = ()
        
    def get_reviews_count(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(reviews_count=Count('reviews__id'))
            return queryset.filter(reviews_count__gte=value)
        
        return queryset