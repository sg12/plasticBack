from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from apps.clinics.models import Clinic
from apps.clinics.serializers import *
from apps.clinics.filters import ClinicFilter
from apps.clinics.yasg import *


class ClinicListView(APIView):
    @doc_clinic_list
    def get(self, request):
        queryset = Clinic.objects.all().order_by('-id')

        filter = ClinicFilter(request.GET, queryset=queryset)

        paginator = LimitOffsetPagination()
        paginator.default_limit = 10
        queryset = paginator.paginate_queryset(filter.qs, request)

        serializer = ClinicListSerializer(queryset, many=True)

        response = Response(serializer.data)
        response.headers['X-Total-Count'] = Clinic.objects.all().count()
        return response


class ClinicRetrieveUpdateView(RetrieveAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicRetrieveSerializer
