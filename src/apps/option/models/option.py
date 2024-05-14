from django.db import models


class Option(models.Model):    
    clinic = models.ForeignKey('clinic.Clinic', on_delete=models.CASCADE, related_name='options')
    category = models.ForeignKey('OptionCategory', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'options'
