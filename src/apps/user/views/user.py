from rest_framework.generics import RetrieveAPIView
from apps.doctor.serializers import *
from apps.clinic.serializers import *
from apps.user.serializers import *
from apps.user.models import User
# from apps.user.schemas import doc_user


# @doc_user
class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_object(self):
        self.kwargs['pk'] = self.kwargs.pop('user_pk')
        return super().get_object()
    