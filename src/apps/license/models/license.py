from django.db import models


class License(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='licenses')
    image = models.ImageField(upload_to='licenses')
    
    class Meta:
        db_table = 'licenses'
    
    def __str__(self) -> str:
        return self.user.email
