class UserUpdate:
    def update(self, instance, validated_data):
        exist = validated_data.get('user')
        if exist:
            user_data = validated_data.pop('user')
            user = instance.user
            user.__dict__.update(user_data)
            user.save()
        
        return super().update(instance, validated_data)
