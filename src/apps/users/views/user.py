from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clients.serializers import ClientRetrieveSerializer
from apps.surgeons.serializers import SurgeonRetrieveSerializer
from apps.clinics.serializers import ClinicReadSerializer
from apps.clients.models import Client
from apps.surgeons.models import Surgeon
from apps.clinics.models import Clinic
from rest_framework.permissions import IsAuthenticated


class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        match request.user.type:
            case 'client':
                serializer = ClientRetrieveSerializer(Client.objects.get(user=request.user))
            case 'surgeon':
                serializer = SurgeonRetrieveSerializer(Surgeon.objects.get(user=request.user))
            case 'clinic':
                serializer = ClinicReadSerializer(Clinic.objects.get(user=request.user))

        return Response(serializer.data)
