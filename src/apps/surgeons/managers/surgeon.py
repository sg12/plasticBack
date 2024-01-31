from django.db import models
from django.db.models import Avg, Count, IntegerField, FloatField, Prefetch
from django.db.models.functions import Coalesce


class SurgeonManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.select_related('user')

        queryset = queryset.annotate(
            rating=Coalesce(
                Avg('user__reviews_about_me__rating'),
                0,
                output_field=FloatField()
            )
        )

        queryset = queryset.prefetch_related('metro')

        queryset = queryset.annotate(
            reviews_count=Coalesce(
                Count('user__reviews_about_me'),
                0,
                output_field=IntegerField()
            )
        )

        return queryset
