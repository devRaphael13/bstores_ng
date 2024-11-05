"""
**************************************** JESUS ****************************************
"""

from rest_framework.viewsets import ReadOnlyModelViewSet
from . import serializers as s
from . import models as m

class ProductViewSet(ReadOnlyModelViewSet):
    queryset = m.Product.objects.select_related("category").prefetch_related("sizes", "colours")
    serializer_class = s.ProductSerializer

    def filter_queryset(self, queryset):
        query = self.request.query_params
        queryset = super().filter_queryset(queryset)

        category = query.get("category", None)

        if category and category != "All":
            queryset = queryset.filter(category__name=category)
            
        return queryset

class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer

class SizeViewSet(ReadOnlyModelViewSet):
    queryset = m.Size.objects.all()
    serializer_class = s.SizeSerializer
class ColourViewSet(ReadOnlyModelViewSet):
    queryset = m.Colour.objects.all()
    serializer_class = s.ColourSerializer
