from rest_framework.views import APIView
from .models import Statiy
from .serializer import StatiySerializer
from rest_framework.response import Response

class GetStatyi(APIView):

    def get(self, request):
        qs = Statiy.objects.all()
        serializer = StatiySerializer(qs, many=True)
        return Response(serializer.data)
    
        