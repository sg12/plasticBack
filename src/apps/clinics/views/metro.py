from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.models import Metro
from apps.clinics.serializers import MetroListSerializer
from apps.clinics.yasg import doc_metro_list

__all__ = ['MetroListView']


class MetroListView(APIView):
    @doc_metro_list
    def get(self, request):
        metro = Metro.objects.all()
        serializer = MetroListSerializer(metro, many=True)

        response = Response(serializer.data)
        response.headers['X-Total-Count'] = len(serializer.data)
        return response