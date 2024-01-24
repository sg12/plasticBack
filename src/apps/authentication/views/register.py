from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import User
from apps.clients.models import Client
from apps.surgeons.models import Surgeon
from apps.clinics.models import Clinic
from apps.authentication.serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.http import Http404
from apps.authentication.yasg import doc_register


class RegisterView(APIView):
    @doc_register
    def post(self, request, type):
        if type not in ['client', 'surgeon', 'clinic']:
            raise Http404

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.data['password'] != serializer.data['re_password']:
            return Response({'detail': {'re_password': "Пароли не совпадают"}})

        user = User(
            email=serializer.data['email'],
            password=make_password(serializer.data['password']),
            type=type
        )
        user.save()

        match type:
            case 'client':
                Client.objects.create(user=user)
            case 'surgeon':
                Surgeon.objects.create(user=user)
            case 'clinic':
                Clinic.objects.create(user=user)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})
