from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.review.managers import ReviewManager


class Review(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(5)))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ReviewManager()
    
    class Meta:
        db_table = 'reviews'
        
    def __str__(self) -> str:
        return f'{self.author.email} -> {self.user.email}'
    
    def get_replies(self):
        return self.replies.all()
