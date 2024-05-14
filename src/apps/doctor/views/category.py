from rest_framework.generics import ListAPIView
from apps.doctor.models import Category
from apps.doctor.serializers import CategorySerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
