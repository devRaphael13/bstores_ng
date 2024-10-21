from rest_framework import serializers as rs
from django.utils.timezone import now
from . import models as m

class ProductSerializer(rs.ModelSerializer):
    new = rs.SerializerMethodField()
    class Meta:
        model = m.Product
        fields = "__all__"

    def get_new(self, obj):
        delta = now().date() - obj.created

        if delta.days < 30:
            return True
        return False
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["sizes"] = [size.size for size in instance.sizes.all()]
        rep["colours"] = [colour.name for colour in instance.colours.all()]
        rep["image"] = instance.image.url
        return rep

class CategorySerializer(rs.ModelSerializer):

    class Meta:
        model = m.Category
        fields = "__all__"

class SizeSerializer(rs.ModelSerializer):
    class Meta:
        model = m.Size
        fields = "__all__"

class ColourSerializer(rs.ModelSerializer):

    class Meta:
        model = m.Colour
        fields = "__all__"
