from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clients.serializers import ClientRetrieveSerializer
from apps.surgeons.serializers import SurgeonRetrieveSerializer
from apps.clinics.serializers import ClinicRetrieveSerializer
from apps.accounts.serializers import UserRetrieveSerializer
from apps.clients.models import Client
from apps.surgeons.models import Surgeon
from apps.clinics.models import Clinic
from rest_framework.permissions import IsAuthenticated
from apps.accounts.yasg import doc_account


class AccountView(APIView):
    permission_classes = [IsAuthenticated]

    @doc_account
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