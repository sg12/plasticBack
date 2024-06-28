from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema_field


class NumberFilter(filters.NumberFilter):
    def filter(self, qs, value):
        qs = super().filter(qs, value)
        qs = qs.filter(user__services__status=True) if value else qs
        return qs


class ClinicFilter(filters.FilterSet):
    specialization = filters.CharFilter(field_name='')
    metro = filters.CharFilter(field_name='metro__slug')
    district = filters.CharFilter(field_name='district__slug')
    city = filters.CharFilter(field_name='city__slug')
    reception = filters.CharFilter(method='get_reception')
    ordering = filters.CharFilter(method='get_ordering')
    
    def get_reception(self, queryset, name, value):
        params = {}
        add_private = lambda: params.update({'private_reception': True})
        add_clinic = lambda: params.update({'clinic_reception': True})
        
        if ',' in value:
            values = value.split(',')
            if 'private' in values:
                add_private()
            if 'clinic' in values:
                add_clinic()
        else:
            match value:
                case 'private':
                    add_private()
                case 'clinic':
                    add_clinic()
        
        queryset = queryset.filter(**params)

        return queryset

    def get_ordering(self, queryset, name, value):
        params = []
        add_rating = lambda: params.append('-rating')
        add_reviews = lambda: params.append('-reviews_count')
        
        if ',' in value:
            values = value.split(',')
            if 'rating' in values:
                add_rating()
            if 'reviews' in values:
                add_reviews()
        else:
            match value:
                case 'rating':
                    add_rating()
                case 'reviews':
                    add_reviews()
        print(params)
        return queryset.order_by(*params)
