from django_filters import rest_framework as filters
from apps.accounts.models import User
from apps.surgeons.models import Surgeon


class SurgeonFilter(filters.FilterSet):
    search = filters.CharFilter(method='get_search')
    specialtie = filters.CharFilter(field_name='specialtie__slug', lookup_expr='exact')
    experience = filters.NumberFilter(lookup_expr='gte')
    category = filters.NumberFilter(lookup_expr='exact')
    academic = filters.NumberFilter(lookup_expr='exact')
    gender = filters.ChoiceFilter(field_name='user__gender', choices=User.GENDERS)
    reception = filters.ChoiceFilter(choices=Surgeon.RECEPTION)
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
        model = Surgeon
        fields = ()