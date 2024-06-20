from django_filters import rest_framework as filters
from apps.user.models import Gender
from apps.doctor.models import Doctor
from apps.reception.models import ReceptionType


class DoctorFilter(filters.FilterSet):
    search = filters.CharFilter(field_name='user__username', lookup_expr='contains')
    specialtie = filters.NumberFilter()
    experience = filters.NumberFilter(lookup_expr='gte')
    category = filters.NumberFilter()
    degree = filters.NumberFilter()
    gender = filters.ModelChoiceFilter(queryset=Gender.objects.all())
    reception_type = filters.ModelChoiceFilter(queryset=ReceptionType.objects.all())
    ordering = filters.CharFilter(method='get_ordering')

    def get_ordering(self, queryset, name, value):
        rating = False
        reviews = False
        
        if ',' in value:
            if 'rating' in value:
                rating = True
            if 'reviews' in value:
                reviews = True
        else:
            if 'rating' in value:
                rating = True
            elif 'reviews' in value:
                reviews = True
        
        if rating:
            queryset = queryset.order_by('-rating')
        if reviews:
            queryset = queryset.order_by('-reviews_count')

        return queryset
    
    class Meta:
        model = Doctor
        fields = ()
