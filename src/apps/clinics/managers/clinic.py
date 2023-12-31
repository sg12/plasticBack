from django.db import models
from django.db.models import Avg, Count, IntegerField, FloatField, Prefetch
from django.db.models.functions import Coalesce


class ClinicManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.select_related('user')

        queryset = queryset.prefetch_related('surgeons', 'metro')

        queryset = queryset.annotate(
            rating=Coalesce(
                Avg('ratings__star'),
                0,
                output_field=FloatField()
            )
        )

        queryset = queryset.annotate(
            reviews_count=Coalesce(
                Count('reviews'),
                0,
                output_field=IntegerField()
            )
        )

        return queryset
