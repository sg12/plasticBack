from rest_framework.serializers import ModelSerializer
from apps.users.models import User


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'gender',
            'avatar',
            'address',
            'phone',
            'date_created',
        )
 