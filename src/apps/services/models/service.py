from django.db import models


class Service(models.Model):
    OPERATION_TYPE = [
        ("BODY", "body"),
        ("FACE", "face"),
        ("OTHER", "other")
    ]
    
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=OPERATION_TYPE)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    
    class Meta:
        db_table = 'services'
        
    def __str__(self) -> str:
        return self.name