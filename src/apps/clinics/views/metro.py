from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.models import Metro
from apps.clinics.serializers import MetroSerializer


class MetroListView(APIView):
    def get(self, request):
        metro = Metro.objects.all()
        serializer = MetroSerializer(metro)
        return Response(serializer.data)