from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.serializers import ClinicRetrieveSerializer
from apps.surgeons.serializers import SurgeonRetrieveSerializer
from apps.clients.serializers import ClientRetrieveSerializer
from apps.surgeons.models import Surgeon
from apps.users.yasg import doc_user_me
from rest_framework.permissions import IsAuthenticated


class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    @doc_user_me
    def get(self, request):
        match request.user.type:
            case 'client':
                serializer = ClientRetrieveSerializer(request.user.client)
            case 'surgeon':
                serializer = SurgeonRetrieveSerializer(Surgeon.objects.get(user=request.user))
            case 'clinic':
                serializer = ClinicRetrieveSerializer(request.user.clinic)

        return Response(serializer.data)
