from django.db import models


class Review(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="clinics_reviews")
    clinic = models.ForeignKey("Clinic", on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    star = models.PositiveSmallIntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    class Meta:
        db_table = "clinic_reviews"
