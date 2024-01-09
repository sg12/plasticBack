from rest_framework.views import APIView
from pkg.api_view.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from apps.clinics.models import Clinic
from apps.clinics.serializers import *
from apps.clinics.filters import ClinicFilter
from apps.clinics.yasg import *


class ClinicListView(APIView):
    @doc_clinic_list
    def get(self, request):
        queryset = Clinic.objects.all()
        filter = ClinicFilter(request.GET, queryset=queryset)
        serializer = ClinicListSerializer(filter.qs, many=True)

        response = Response(serializer.data)
        response.headers['X-Total-Count'] = len(serializer.data)
        return response


class ClinicRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Clinic.objects.all()
    retrieve_serializer = ClinicReadSerializer
    update_serializer = ClinicUpdateSerializer

    def return_response(self):
        instance = self.get_object()
        serializer = self.retrieve_serializer(instance=instance)
        return Response(serializer.data)

    @doc_clinic_update
    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)
        return self.return_response()

    @doc_clinic_update
    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        return self.return_response()
