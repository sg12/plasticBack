from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.models import District
from apps.clinics.serializers import DistrictSerializer


__all__ = ['DistrictListView']


class DistrictListView(APIView):
    def get(self, request):
        metro = District.objects.all()
        serializer = DistrictSerializer(metro)
        return Response(serializer.data)