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

    def return_serialize_record(self):
        instance = self.get_object()
        serializer = SurgeonRetrieveSerializer(instance=instance)
        return Response(serializer.data)

    @doc_surgeon_retrieve_update
    def update(self, request, *args, **kwargs):
        super().update()
        self.return_serialize_record()

    @doc_surgeon_retrieve_update
    def partial_update(self, request, *args, **kwargs):
        super().partial_update()
        self.return_serialize_record()
