from apps.clinics.models import Clinic
from django.db.models import Avg, Count, IntegerField, FloatField, Prefetch
from django.db.models.functions import Coalesce
from apps.surgeons.queryset import surgeon_queryset


# queryset = (
#     Clinic.objects.all().
#     prefetch_related('metro', Prefetch('surgeons', queryset=surgeon_queryset.filter(clinic))).
#     annotate(rating=Coalesce(Avg('ratings__star'), 0, output_field=FloatField())).
#     annotate(reviews_count=Coalesce(Count('reviews'), 0, output_field=IntegerField()))
# )
#
# def get_queryset