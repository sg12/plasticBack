from django.db import models
from .base import BaseLocation


class District(BaseLocation):
    class Meta:
        db_table = 'districts'
        
    