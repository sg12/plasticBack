from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.models import District
from apps.clinics.serializers import DistrictListSerializer
from apps.clinics.yasg import doc_district_list

__all__ = ['DistrictListView']


class DistrictListView(APIView):
    @doc_district_list
    def get(self, request):
        metro = District.objects.all()
        serializer = DistrictListSerializer(metro, many=True)
        return Response(serializer.data)