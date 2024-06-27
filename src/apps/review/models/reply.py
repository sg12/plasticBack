from django.db import models


class Reply(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    review = models.OneToOneField("Review", on_delete=models.CASCADE, related_name='reply')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "review_replies"

    def __str__(self) -> str:
        return f'{self.author.email} -> ({self.review.author.email}){self.review.text[:10]}'
