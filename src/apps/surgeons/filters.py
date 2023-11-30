from django_filters import rest_framework as filters
from apps.surgeons.models import Surgeon
from apps.users.models import User
from django.db.models import Count
from .models import Surgeon


class SurgeonFilter(filters.FilterSet):
    experience = filters.NumberFilter(lookup_expr='gte')
    category = filters.NumberFilter(lookup_expr='exact')
    academic = filters.NumberFilter(lookup_expr='exact')
    gender = filters.ChoiceFilter(choices=User.GENDERS)
    reception = filters.ChoiceFilter(choices=Surgeon.RECEPTION)
    reviews_count = filters.RangeFilter()
    rating = filters.NumberFilter(lookup_expr='gte')
    
    class Meta:
        model = Surgeon
        fields = ()