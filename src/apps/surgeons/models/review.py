from django.db import models


class Review(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="surgeons_reviews")
    surgeon = models.ForeignKey("Surgeon", on_delete=models.CASCADE, related_name="reviews")
    star = models.PositiveSmallIntegerField(default=0)
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    class Meta:
        db_table = "surgeon_reviews"