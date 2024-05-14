from pkg.generics import RetrieveUpdateAPIView
from apps.user.serializers import *
from rest_framework.permissions import IsAuthenticated


class MeView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer
    result_class = UserSerializer

    def get_object(self):
        return self.request.user
