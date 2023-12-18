from django_filters import rest_framework as filters
from apps.clinics.models import Clinic


class ClinicFilter(filters.FilterSet):
    service = filters.CharFilter(method='get_services')
    spec = filters.CharFilter(field_name='surgeons__specialtie__name', lookup_expr='exact') # Специальность врача
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
        return queryset.filter(surgeons__services__service__slug=value)