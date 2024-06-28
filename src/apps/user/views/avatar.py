from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.user.serializers import *
from apps.user.schemas import doc_avatar


@doc_avatar
class UploadAvatarView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AvatarSerializer
    http_method_names = ['patch']
    
    def get_object(self):
        return self.request.user
