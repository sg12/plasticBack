from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from apps.doctor.serializers import *
from apps.clinic.serializers import *
from apps.user.serializers import *
from apps.doctor.models import Doctor
from apps.clinic.models import Clinic
from apps.user.permissions import IsAdminOrAuthenticated
from apps.user.schemas import doc_user
from django.utils.decorators import method_decorator
from apps.user.decorators import access_type


@doc_user
@method_decorator(access_type, name='dispatch')
class UserView(RetrieveUpdateAPIView):
    permission_classes = (IsAdminOrAuthenticated,)
    serializer_class = UserSerializer

    http_method_names = ('get', 'patch')

    def get_serializer(self, *args, **kwargs):
        user = self.request.user

        match user.type:
            case 'doctor':
                serializer = DoctorSerializer(Doctor.objects.get(user=user), **kwargs)
            case 'clinic':
                serializer = ClinicSerializer(Clinic.objects.get(user=user), **kwargs)
            case _:
                serializer = GenericUserSerializer(user, **kwargs)

        return serializer


    def retrieve(self, request, **kwargs):
        serializer = self.get_serializer(partial=True)
        return Response(serializer.data)

    def update(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        pk = instance.pk

        match type:
            case 'doctor':
                serializer = DoctorSerializer(Doctor.objects.get(pk=pk))
            case 'clinic':
                serializer = ClinicSerializer(Clinic.objects.get(pk=pk))
            case _:
                serializer = GenericUserSerializer(user)

        return Response(serializer.data)
