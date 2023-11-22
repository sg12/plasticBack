from django.db import models


class Surgeon(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='surgeon')
    clinic = models.ForeignKey('Clinic', on_delete=models.SET_NULL, related_name='surgeons', null=True)
    address = models.CharField(max_length=255)
    description = models.TextField()
    license = models.ImageField(upload_to='doctors/licenses/')
    site = models.URLField()
    seniority = models.IntegerField()
    
    
    class Meta:
        db_table = 'surgeons'
    
    def __str__(self) -> str:
        return self.user.username