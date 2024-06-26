from django_filters import rest_framework as filters
from apps.user.models import Gender
from apps.doctor.models import Doctor
from apps.reception.models import ReceptionType


class DoctorFilter(filters.FilterSet):
    specialtie = filters.NumberFilter()
    experience = filters.NumberFilter(lookup_expr='gte')
    category = filters.NumberFilter()
    degree = filters.NumberFilter()
    reception = filters.CharFilter(method='get_reception')
    ordering = filters.CharFilter(method='get_ordering')
    gender = filters.ModelChoiceFilter(
        queryset=Gender.objects.all(),
        to_field_name='name'
    )
    
    def get_reception(self, queryset, name, value):
        private = False
        clinic = False
        
        if '+' in value:
            values = value.split('+')
            if 'private' in values:
                private = True
            if 'clinic' in values:
                clinic = True
        else:
            match value:
                case 'private':
                    private = True
                case 'clinic':
                    clinic = True
        
        if private:
            queryset = queryset.filter(private_reception=True)
        if clinic:
            queryset = queryset.filter(clinic_reception=True)

        return queryset

    def get_ordering(self, queryset, name, value):
        rating = False
        reviews = False
        
        if '+' in value:
            values = value.split('+')
            if 'rating' in values:
                rating = True
            if 'reviews' in values:
                reviews = True
        else:
            match value:
                case 'rating':
                    rating = True
                case 'reviews':
                    reviews = True
        
        if rating:
            queryset = queryset.order_by('-rating')
        if reviews:
            queryset = queryset.order_by('-reviews_count')

        return queryset
    
    class Meta:
        model = Doctor
        fields = ()
