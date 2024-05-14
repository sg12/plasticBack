from django.db import models


class QRCode(models.Model):
    image = models.ImageField(upload_to='qrcode')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'qrcodes'
