from django_filters import rest_framework as filters
from apps.doctor.models import Doctor


class DoctorFilter(filters.FilterSet):
    specialtie = filters.NumberFilter()
    experience = filters.NumberFilter(lookup_expr='gte')
    category = filters.NumberFilter()
    degree = filters.NumberFilter()
    reception = filters.CharFilter(method='get_reception')
    ordering = filters.CharFilter(method='get_ordering')
    gender = filters.ChoiceFilter(field_name='user__gender', choices=(
        ('male', 'male'),
        ('female', 'female')
    ))
    
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
        
        return queryset.order_by(*params)
