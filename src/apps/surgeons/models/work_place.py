from django.db import models
from apps.surgeons.validators import experience_validator


class WorkPlace(models.Model):
    surgeon = models.ForeignKey("Surgeon", on_delete=models.CASCADE, related_name="work_places")
    place = models.CharField(max_length=255)
    posts = models.JSONField(default=dict, validators=[experience_validator])

    class Meta:
        db_table = 'surgeon_experience'