from django.db import models
from apps.clinics.validators.surgeon import experience_validator


class Experience(models.Model):
    surgeon = models.ForeignKey("Surgeon", on_delete=models.CASCADE, related_name="experiences")
    place = models.CharField(max_length=255)
    posts = models.JSONField(default=dict, validators=[experience_validator])

    class Meta:
        db_table = 'surgeon_experience'