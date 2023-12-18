from django.db import models


class License(models.Model):
    surgeon = models.ForeignKey('Clinic', on_delete=models.CASCADE, related_name='licenses')
    image = models.ImageField(upload_to='surgeons/licenses')