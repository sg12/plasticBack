from django.db import models
from django.db.models import Avg, Count, IntegerField, FloatField, Prefetch
from django.db.models.functions import Coalesce


class SurgeonManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.select_related('user', 'clinic')

        queryset = queryset.annotate(
            rating=Coalesce(
                Avg('reviews__star'),
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
