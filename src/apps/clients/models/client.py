from django.db import models


class Client(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='client')
    date_born = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        
    def __str__(self) -> str:
        return self.user.email