from django.db import models
from .base import BaseLocation


class City(BaseLocation):
    class Meta:
        db_table = 'cities'
