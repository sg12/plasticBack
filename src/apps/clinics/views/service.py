from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.models import Service
from apps.clinics.serializers import ServiceSerializer
    

class ServiceListView(APIView):
    def get(self, request):
        metro = Service.objects.all()
        serializer = ServiceSerializer(metro)
        return Response(serializer.data)