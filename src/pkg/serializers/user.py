from rest_framework import serializers


class UserUpdate:
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        if user_data:
            user = instance.user
            user.__dict__.update(user_data)
            user.save()
        
        return super().update(instance, validated_data)
