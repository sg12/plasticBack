from django.db import models


class Review(models.Model):
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    surgeon = models.ForeignKey("Surgeon", on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    class Meta:
        db_table = "surgeon_reviews"