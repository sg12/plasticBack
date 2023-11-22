from django.db import models 


class Education(models.Model):
    surgeon = models.ForeignKey("Surgeon", on_delete=models.CASCADE, related_name="educations")
    place = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'surgeon_educations'