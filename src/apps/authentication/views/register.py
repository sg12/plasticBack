from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.models import User
from apps.authentication.serializers import RegisterSerializer, TokenSerializer
from rest_framework.authtoken.models import Token
from apps.authentication.schemas import doc_register


@doc_register
class RegisterView(APIView):
    def post(self, request, role):
        if not role:
            return Response(status=404)
        
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.data
        data.pop('re_password')

        user = User.objects.create_user(**data, role_name=role)

        token, _ = Token.objects.get_or_create(user=user)
        serializer = TokenSerializer(instance=token)
        
        return Response(status=201, data=serializer.data)
