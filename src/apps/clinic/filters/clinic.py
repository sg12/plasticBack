from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema_field


class NumberFilter(filters.NumberFilter):
    def filter(self, qs, value):
        qs = super().filter(qs, value)
        qs = qs.filter(user__services__status=True) if value else qs
        return qs


# TODO: что за специализация

class ClinicFilter(filters.FilterSet):
    # specialization = filters.CharFilter(field_name='')
    metro = filters.CharFilter(field_name='metro__slug')
    district = filters.CharFilter(field_name='district__slug')
    city = filters.CharFilter(field_name='city__slug')
    ordering = filters.CharFilter(method='get_ordering')

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
