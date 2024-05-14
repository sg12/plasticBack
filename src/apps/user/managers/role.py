from django.db import models


class RoleManager(models.Manager):
    def init_roles(self):
        roles = ['CLIENT', 'DOCTOR', 'CLINIC', 'ADMIN']
        
        for role in roles:
            obj = self.filter(name=role).first()
            if obj:
                continue
            
            r = self.model(name=role)
            r.save()
        