from django.db import models


class Service(models.Model):
    TYPE_OF_OPERATION = [
        ("BODY", "body"),
        ("FACE", "face"),
        ("OTHER", "other")
    ]
    
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=TYPE_OF_OPERATION)
    
    class Meta:
        db_table = 'services'
        
    def __str__(self) -> str:
        return self.name