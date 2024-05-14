from django.db import models 


class Education(models.Model):
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, related_name="educations")
    place = models.CharField(max_length=255)
    date = models.DateField()
    
    class Meta:
        db_table = 'doctor_educations'
