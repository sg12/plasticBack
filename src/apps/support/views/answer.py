from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.support.models import Answer
from apps.support.serializers import *


class AnswerView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    result_class = AnswerSerializer


class AnswerDetailView(UpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerUpdateSerializer
    result_class = AnswerSerializer
