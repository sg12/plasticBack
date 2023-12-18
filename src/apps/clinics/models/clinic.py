from django.db import models
from apps.clinics.managers import ClinicManager


class Clinic(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='clinic')
    director = models.CharField(max_length=50, null=True, blank=True)
    metro = models.ManyToManyField('Metro', related_name='clinics', blank=True)
    open_time = models.TimeField(null=True, blank=True) # открыто с 9:00
    close_time = models.TimeField(null=True, blank=True) # открыто до 21:00
    description = models.TextField(null=True, blank=True)
    specialization = models.TextField(null=True, blank=True)

    objects = ClinicManager()

    # surgeons
    # worktimes
    # ratings
    # reviews
    
    def get_services(self, slug=None):
        all_services = []
        
        for surgeon in self.surgeons.all():
            if slug:
                queryset = (
                    surgeon.services.select_related('service').
                    annotate(service_name=models.F('service__name')).
                    annotate(service_slug=models.F('service__slug')).
                    filter(service_slug=slug)
                )
            else:
                queryset = (
                    surgeon.services.select_related('service').
                    annotate(service_name=models.F('service__name')).
                    annotate(service_slug=models.F('service__slug')).
                    all()
                )
            
            data = [el for el in queryset if el not in all_services]
            
            if len(data) > 0:
                all_services.append(*data)  
        
        return all_services
            
            
            
     
    class Meta:
        db_table = 'clinics'