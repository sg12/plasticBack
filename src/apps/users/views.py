from rest_framework import views, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import RegisterSerializer


class RegisterAPIView(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=400)
        
        serializer.save()
        
        user = User.objects.get(username=serializer.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({"token": token.key})