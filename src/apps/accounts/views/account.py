from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clients.serializers import *
from apps.surgeons.serializers import *
from apps.clinics.serializers import *
from apps.accounts.serializers import *
from apps.accounts.models import User
from apps.clients.models import Client
from apps.surgeons.models import Surgeon
from apps.clinics.models import Clinic
from rest_framework.permissions import IsAuthenticated
from apps.accounts.yasg import *
from django.shortcuts import get_object_or_404


class AccountView(APIView):
    permission_classes = (IsAuthenticated,)

    @doc_account_retrieve
    def get(self, request, **kwargs):
        user_id = kwargs.get('user_id')

        if user_id is None:
            user = request.user
        else:
            user = get_object_or_404(User, pk=user_id)

        match user.type:
            case 'client':
                serializer = ClientRetrieveSerializer(Client.objects.get(user=user))
            case 'surgeon':
                serializer = SurgeonRetrieveSerializer(Surgeon.objects.get(user=user))
            case 'clinic':
                serializer = ClinicRetrieveSerializer(Clinic.objects.get(user=user))
            case _:
                serializer = UserRetrieveSerializer(request.user)

        return Response(serializer.data)

    def update(self, request, **kwargs):
        pk = kwargs.get('pk')

        if pk is None:
            user = request.user
        else:
            user = get_object_or_404(User, pk=pk)

        partial = kwargs.pop('partial', False)
        user_data = request.data.pop('user', {})
        type = request.user.type

        user_serializer = UserUpdateSerializer(instance=user, data=user_data, partial=partial)
        user_serializer.is_valid(raise_exception=True)

        if type in ['client', 'surgeon', 'clinic']:
            match type:
                case 'client':
                    serializer = ClientUpdateSerializer(instance=user.client, data=request.data, **kwargs)
                case 'surgeon':
                    serializer = SurgeonUpdateSerializer(instance=user.surgeon, data=request.data, **kwargs)
                case 'clinic':
                    serializer = ClinicUpdateSerializer(instance=user.clinic, data=request.data, **kwargs)

            serializer.is_valid(raise_exception=True)
            instance = serializer.save()

        user_serializer.save()

        pk = instance.pk
        instance = None

        match type:
            case 'client':
                instance = Client.objects.get(pk=pk)
            case 'surgeon':
                instance = Surgeon.objects.get(pk=pk)
            case'clinic':
                instance = Clinic.objects.get(pk=pk)

        match type:
            case 'client':
                serializer = ClientRetrieveSerializer(instance=instance)
            case 'surgeon':
                serializer = SurgeonRetrieveSerializer(instance=instance)
            case 'clinic':
                serializer = ClinicRetrieveSerializer(instance=instance)

        return Response(serializer.data)

    @doc_account_update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @doc_account_update
    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)