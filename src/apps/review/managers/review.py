from django.db import models
from django.db.models import F
from django.db.models.functions import Coalesce
from django.apps import apps


class ReviewManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('reply')
        return queryset
