from django.db import models


class Rating(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='ratings')
    surgeon = models.ForeignKey('Surgeon', on_delete=models.CASCADE, related_name='ratings')
    star = models.PositiveSmallIntegerField()
    
    class Meta:
        db_table = 'surgeon_ratings'