from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema_field


class NumberFilter(filters.NumberFilter):
    def filter(self, qs, value):
        qs = super().filter(qs, value)
        qs = qs.filter(user__services__status=True)
        return qs


class ClinicFilter(filters.FilterSet):
    private_reception = filters.BooleanFilter(help_text='Частный прием')
    clinic_reception = filters.BooleanFilter(help_text='Прием в клинике')
    metro = filters.CharFilter(field_name='metro__slug', help_text='Ближайщее метро')
    district = filters.CharFilter(field_name='district__slug', help_text='Район')
    city = filters.CharFilter(field_name='city__slug', help_text='Город')
    price_min = NumberFilter(
        field_name='user__services__price', 
        lookup_expr='gte',
        help_text='Минимальная цена за услугу'
    )
    price_max = NumberFilter(
        field_name='user__services__price', 
        lookup_expr='lte',
        help_text='Максимальная цена за услугу'
    )
