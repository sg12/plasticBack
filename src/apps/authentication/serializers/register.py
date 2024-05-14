from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps.user.models import User
from django.utils.translation import gettext as _


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, validators=(UniqueValidator(queryset=User.objects.all()),))
    password = serializers.CharField(required=True)
    re_password = serializers.CharField(required=True)
    
    def validate(self, attr):
        password = attr['password']
        re_password = attr['re_password']
        
        if password != re_password:
            err = _('Passwords must be the same')
            raise serializers.ValidationError({
                'password': err, 
                're_password': err
            })
        
        return attr
