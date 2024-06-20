from rest_framework.generics import ListAPIView
from apps.faq.models import FAQ
from apps.faq.serializers import FAQSerializer
from apps.faq.schemas import doc_faq


@doc_faq
class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
