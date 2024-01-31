from django.db import models


class Review(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="my_reviews")
    target = models.ForeignKey("User", on_delete=models.CASCADE, related_name="reviews_about_me")
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    class Meta:
        db_table = "reviews"
