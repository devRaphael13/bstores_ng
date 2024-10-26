"""
**************************************** JESUS ****************************************
"""

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import serializers as s
from . import models as m

class ProductViewSet(ModelViewSet):
    queryset = m.Product.objects.all()
    serializer_class = s.ProductSerializer

    def filter_queryset(self, queryset):
        query = self.request.query_params
        queryset = super().filter_queryset(queryset)

        category = query.get("category", None)

        if category and category != "All":
            queryset = queryset.filter(category__name=category)
            
        return queryset

class CategoryViewSet(ModelViewSet):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer

class SizeViewSet(ModelViewSet):
    queryset = m.Size.objects.all()
    serializer_class = s.SizeSerializer
class ColourViewSet(ModelViewSet):
    queryset = m.Colour.objects.all()
    serializer_class = s.ColourSerializer
