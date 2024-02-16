from django_filters import rest_framework as filters
from apps.clinics.models import Clinic


class ClinicFilter(filters.FilterSet):
    search = filters.CharFilter(method='get_search')
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
        if value == 'rating':
            queryset = queryset.order_by('-rating')
        elif value == 'reviews':
            queryset = queryset.order_by('-reviews_count')
        
        return queryset

    def get_services(self, queryset, name, value):
        return queryset.filter(user__services__service_info__slug=value, user__services__status=True)

    def get_search(self, queryset, name, value):
        return queryset.filter(user__username__contains=value)