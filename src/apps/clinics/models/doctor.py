from django.db import models


class Doctor(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    description = models.TextField()
    services = models.ManyToManyField('Service')
    license = models.ImageField(upload_to='doctors/licenses/')
    site = models.URLField()
    
    class Meta:
        db_table = 'doctors'
    
    def __str__(self) -> str:
        return self.user.username