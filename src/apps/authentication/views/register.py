from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.models import User, Role
from apps.authentication.serializers import RegisterSerializer, TokenSerializer
from rest_framework.authtoken.models import Token
from apps.authentication.schemas import doc_register


@doc_register
class RegisterView(APIView):
    def post(self, request, role):
        try:
            Role.objects.get(name=role)
        except Role.DoesNotExist:
            return Response(status=400, data={'detail': 'Вы указали неправильную роль'})
        
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.data
        data.pop('re_password')

        user = User.objects.create_user(**data, role_name=role)

        token, _ = Token.objects.get_or_create(user=user)
        serializer = TokenSerializer(instance=token)
        
        return Response(status=201, data=serializer.data)
