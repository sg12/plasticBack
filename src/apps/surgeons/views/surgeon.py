from rest_framework.response import Response
from apps.surgeons.models import Surgeon
from apps.surgeons.serializers import *
from apps.surgeons.filters import SurgeonFilter
from rest_framework.views import APIView
from pkg.api_view.generics import RetrieveUpdateAPIView
from apps.surgeons.yasg import *


class SurgeonListView(APIView):
    @doc_surgeon_list
    def get(self, request):
        queryset = Surgeon.objects.all()
        filter = SurgeonFilter(request.GET, queryset=queryset)
        serializer = SurgeonListSerializer(filter.qs, many=True)
        return Response(serializer.data)
    

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
