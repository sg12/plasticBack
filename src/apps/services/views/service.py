from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from apps.services.models import ServiceInfo
from apps.accounts.models import User
from apps.services.serializers import ServiceInfoListSerializer
from apps.clinics.serializers import ClinicListSerializer
from apps.services.yasg import doc_service_slug_get


class ServiceInfoListView(ListAPIView):
    queryset = ServiceInfo.objects.all()
    serializer_class = ServiceInfoListSerializer


# Refactor
class SearchClinicByServiceSlugView(APIView):
    @doc_service_slug_get
    def get(self, request, slug):
        queryset = User.objects.filter(type='clinic', services__service__slug=slug)
        serializer = ClinicListSerializer(instance=queryset, many=True)
        return Response(serializer.data)