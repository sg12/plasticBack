from pkg.views.read import ReadAPIView
from apps.articles.models import Category
from apps.articles.serializers import CategorySerializer


class CategoryReadView(ReadAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer