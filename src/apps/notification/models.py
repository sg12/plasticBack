from django.db import models

class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    theme = models.CharField(max_length=100)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notification'
        

