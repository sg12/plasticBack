from rest_framework.views import APIView
from rest_framework.response import Response
from apps.accounts.models import User
from rest_framework.authtoken.models import Token
from apps.authentication.serializers import AuthSerializer
from django.contrib.auth.hashers import check_password
from apps.authentication.yasg import doc_login


fail_auth = {
    'detail': {
        'email': 'Неверные данные для входа',
        'password': 'Неверные данные для входа'
    }
}


class LoginView(APIView):
    @doc_login
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = User.objects.filter(email=serializer.data['email']).first()
        
        if not user:
            return Response(fail_auth, status=400)
        
        if not check_password(serializer.data['password'], user.password):
            return Response(fail_auth, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key})
