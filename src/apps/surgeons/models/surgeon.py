from django.db import models


class Surgeon(models.Model):
    RECEPTION = (
        ('CLINIC', 'clinic'),
        ('PRIVATE', 'private')
    )
    
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='surgeon')
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.SET_NULL, related_name='surgeons', null=True, blank=True)
    specialtie = models.ForeignKey('Specialtie', on_delete=models.PROTECT, related_name='surgeons')
    description = models.TextField()
    license = models.ImageField(upload_to='doctors/licenses/')
    experience = models.IntegerField() # стаж
    category = models.IntegerField()
    academic = models.IntegerField() # ученая степень
    reception = models.CharField(max_length=20, choices=RECEPTION)
    # educations
    # reviews
    # work_places
    # services
    # ratings
    
    @property
    def rating(self):
        data = self.ratings.aggregate(rating=models.Avg('star'))
        return data['rating']
        
    
    class Meta:
        db_table = 'surgeons'