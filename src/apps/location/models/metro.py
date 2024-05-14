from .base import BaseLocation


class Metro(BaseLocation):
    class Meta:
        db_table = 'metro'
