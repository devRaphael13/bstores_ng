from rest_framework import serializers as rs
from . import models as m

class ProductSerializer(rs.ModelSerializer):

    class Meta:
        model = m.Product
        fields = "__all__"


class CategorySerializer(rs.ModelSerializer):

    class Meta:
        model = m.Category
        fields = "__all__"
        