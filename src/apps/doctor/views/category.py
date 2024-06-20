from rest_framework.generics import ListAPIView
from apps.doctor.models import Category
from apps.doctor.serializers import CategorySerializer
from apps.doctor.schemas import doc_category


@doc_category
class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
