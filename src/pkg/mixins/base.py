from rest_framework.serializers import BaseSerializer


class BaseModelMixin:    
    result_class: BaseSerializer = None
