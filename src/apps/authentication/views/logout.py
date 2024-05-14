from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from apps.authentication.schemas import doc_logout


@doc_logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        token = Token.objects.filter(user=request.user)

        if token:
            token.delete()
        
        return Response({'message': 'Вы успешно вышли из аккаунта'})
