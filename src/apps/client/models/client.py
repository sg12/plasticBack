from django.db import models


class Client(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='client')
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_born = models.DateField(null=True, blank=True)
    discount = models.PositiveSmallIntegerField(null=True, blank=True)
    qrcode = models.ForeignKey('QRCode', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = 'clients'
        
    def __str__(self) -> str:
        return str(self.user.email)
