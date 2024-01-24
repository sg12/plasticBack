from rest_framework.generics import ListAPIView
from apps.faq.models import FAQ
from apps.faq.serializers import FAQListSerializer


class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQListSerializer
