from django_filters import rest_framework as filters
from apps.user.models import Gender
from apps.doctor.models import Doctor
from apps.reception.models import ReceptionType


class DoctorFilter(filters.FilterSet):
    search = filters.CharFilter(method='get_search')
    specialtie = filters.CharFilter(field_name='specialtie__slug', lookup_expr='exact')
    experience = filters.NumberFilter(lookup_expr='gte')
    category = filters.NumberFilter(lookup_expr='exact')
    degree = filters.NumberFilter(lookup_expr='exact')
    gender = filters.ModelChoiceFilter(field_name='gender__slug', queryset=Gender.objects.all())
    reception_type = filters.ModelChoiceFilter(field_name='reception_type__slug', queryst=ReceptionType.objects.all())
    reviews = filters.NumberFilter(lookup_expr='gte')
    rating = filters.NumberFilter(lookup_expr='gte')
    sort = filters.CharFilter(method='get_sort')

    def get_sort(self, queryset, name, value):
        if value == 'rating':
            queryset = queryset.order_by('-rating')
        elif value == 'reviews':
            queryset = queryset.order_by('-reviews_count')

        return queryset

    def get_search(self, queryset, name, value):
        return queryset.filter(user__username__contains=value)
    
    class Meta:
        model = Doctor
        fields = ()
