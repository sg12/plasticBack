from apps.user.models import User
from .user import BaseUserFields


class GeneralAuthorSerializer(BaseUserFields):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'avatar'
        )
