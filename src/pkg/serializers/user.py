class CurrentUserDefault:
    requires_context = True
    user_field = None
    
    def __init__(self, user_field: str = None):
        self.user_field = user_field

    def __call__(self, serializer_field):
        user = serializer_field.context['request'].user
        
        if self.user_field:
            return getattr(user, self.user_field)
        
        return user

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class UserUpdate:
    def update(self, instance, validated_data):
        exist = validated_data.get('user')
        if exist:
            user_data = validated_data.pop('user')
            user = instance.user
            user.__dict__.update(user_data)
            user.save()
        
        return super().update(instance, validated_data)
