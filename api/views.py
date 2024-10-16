from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import serializers as s
from . import models as m

class ProductViewSet(ModelViewSet):
    queryset = m.Product.objects.all()
    serializer_class = s.ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer

