from django_filters import rest_framework as filters
from apps.clinics.models import Clinic


class ClinicFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    address = filters.CharFilter(lookup_expr='icontains')
    metro = filters.CharFilter(field_name='metro__name', lookup_expr='icontains')
    # services = filters.CharFilter(field_name='services__name', lookup_expr='icontains')
    type = filters.CharFilter(field_name='type__name', lookup_expr='icontains')
    price = filters.RangeFilter()
    
    class Meta:
        model = Clinic
        fields = (
            'name',
            'address',
            'metro__name',
            # 'services__name',
            'type__name',
        )