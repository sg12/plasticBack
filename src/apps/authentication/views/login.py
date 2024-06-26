from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.models import User
from rest_framework.authtoken.models import Token
from apps.authentication.serializers import LoginSerializer, TokenSerializer
from django.contrib.auth.hashers import check_password
from apps.authentication.schemas import doc_login


FAIL_AUTH = {
    'detail': {
        'errors': ['Неверные данные для входа']
    }
}


@doc_login
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = User.objects.filter(email=serializer.data['email']).first()
        
        if not user:
            return Response(FAIL_AUTH, status=400)
        
        if not check_password(serializer.data['password'], user.password):
            return Response(FAIL_AUTH, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        serializer = TokenSerializer(instance=token)
        
        return Response(status=201, data=serializer.data)
