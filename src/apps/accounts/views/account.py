from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clients.serializers import *
from apps.surgeons.serializers import *
from apps.clinics.serializers import *
from apps.accounts.serializers import *
from apps.clients.models import Client
from apps.surgeons.models import Surgeon
from apps.clinics.models import Clinic
from rest_framework.permissions import IsAuthenticated
from apps.accounts.yasg import *


class AccountView(APIView):
    permission_classes = (IsAuthenticated,)

    @doc_account_retrieve
    def get(self, request):
        match request.user.type:
            case 'client':
                serializer = ClientRetrieveSerializer(Client.objects.get(user=request.user))
            case 'surgeon':
                serializer = SurgeonRetrieveSerializer(Surgeon.objects.get(user=request.user))
            case 'clinic':
                serializer = ClinicRetrieveSerializer(Clinic.objects.get(user=request.user))
            case _:
                serializer = UserRetrieveSerializer(request.user)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user_data = request.data.pop('user', {})

        user_serializer = UserUpdateSerializer(instance=request.user, data=user_data, partial=partial)
        user_serializer.is_valid(raise_exception=True)

        clinic_serializer = ClinicUpdateSerializer(instance=request.user.clinic, data=request.data, **kwargs)
        clinic_serializer.is_valid(raise_exception=True)

        user_serializer.save()
        clinic_serializer.save()

        clinic = Clinic.objects.get(pk=request.user.clinic.pk)
        serializer = ClinicRetrieveSerializer(clinic)

        return Response(serializer.data)

    @doc_account_update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @doc_account_update
    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)