from rest_framework.generics import ListAPIView
from apps.option.models import Option
from apps.option.serializers import OptionSerializer

# TODO: Возможность добавлять опции на клинику и изменять их

class OptionView(ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
