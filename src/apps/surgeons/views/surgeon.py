from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from apps.surgeons.models import Surgeon
from apps.surgeons.serializers import *
from apps.surgeons.filters import SurgeonFilter
from pkg.pagination import PagePagination
from apps.surgeons.yasg import *


class SurgeonListView(APIView):
    @doc_surgeon_list
    def get(self, request):
        queryset = Surgeon.objects.all().order_by('-id')

        filter = SurgeonFilter(request.GET, queryset=queryset)

        queryset = PagePagination().paginate_queryset(filter.qs, request)

        serializer = SurgeonListSerializer(queryset, many=True)

        response = Response(serializer.data)
        response.headers['X-Total-Count'] = filter.qs.count()
        response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
        return response
    

class SurgeonRetrieveUpdateView(RetrieveAPIView):
    queryset = Surgeon.objects.all()
    serializer_class = SurgeonRetrieveSerializer
