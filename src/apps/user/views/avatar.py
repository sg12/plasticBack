from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.user.serializers import *
from rest_framework.parsers import MultiPartParser
from apps.user.schemas import doc_avatar


@doc_avatar
class UploadAvatarView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    serializer_class = AvatarSerializer
    http_method_names = ['patch']
    
    def get_object(self):
        return self.request.user
