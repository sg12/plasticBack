from rest_framework.response import Response
from rest_framework.views import APIView
from pkg.generics import RetrieveUpdateAPIView
from apps.surgeons.models import Surgeon
from apps.surgeons.serializers import *
from apps.surgeons.filters import SurgeonFilter
from rest_framework.pagination import LimitOffsetPagination
from apps.surgeons.yasg import *


class SurgeonListView(APIView):
    @doc_surgeon_list
    def get(self, request):
        queryset = Surgeon.objects.all().order_by('-id')

        filter = SurgeonFilter(request.GET, queryset=queryset)

        paginator = LimitOffsetPagination()
        paginator.default_limit = 10
        queryset = paginator.paginate_queryset(filter.qs, request)

        serializer = SurgeonListSerializer(queryset, many=True)

        response = Response(serializer.data)
        response.headers['X-Total-Count'] = len(serializer.data)
        return response
    

class SurgeonRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Surgeon.objects.all()
    retrieve_serializer = SurgeonRetrieveSerializer
    update_serializer = SurgeonUpdateSerializer

    def return_response(self):
        instance = self.get_object()
        serializer = self.retrieve_serializer(instance=instance)
        return Response(serializer.data)

    @doc_surgeon_retrieve_update
    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)
        return self.return_response()

    @doc_surgeon_retrieve_update
    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        return self.return_response()
