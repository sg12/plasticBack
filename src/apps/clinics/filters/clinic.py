from django_filters import rest_framework as filters
from apps.clinics.models import Clinic


class ClinicFilter(filters.FilterSet):
    service = filters.CharFilter(method='get_services', lookup_expr='exact')
    reception = filters.ChoiceFilter(choices=Clinic.RECEPTION)
    price = filters.RangeFilter(field_name='user__services__price')
    metro = filters.CharFilter(field_name='metro__slug', lookup_expr='exact')
    district = filters.CharFilter(field_name='district__slug', lookup_expr='exact')
    sort = filters.CharFilter(method='get_sort')
    
    class Meta:
        model = Clinic
        fields = ()
        
    def get_sort(self, queryset, name, value):
        if value == 'rating' or value == '-rating':
            queryset = queryset.order_by(value)
        elif value == 'reviews' or value == '-reviews':
            queryset = queryset.order_by(value+'_count', 'name')
        
        return queryset

    def get_services(self, queryset, name, value):
        return queryset.filter(user__services__service_info__slug=value, user__services__active=True)
