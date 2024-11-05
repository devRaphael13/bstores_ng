from rest_framework import serializers as rs
from django.utils.timezone import now
from . import models as m


class ReadOnlyModelSerializer(rs.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        setattr(self.Meta, 'read_only_fields', [*self.fields])

class ProductSerializer(ReadOnlyModelSerializer):
    new = rs.SerializerMethodField()
    image = rs.SerializerMethodField()

    category = rs.StringRelatedField()
    sizes = rs.StringRelatedField(many=True)
    colours = rs.StringRelatedField(many=True)
    class Meta:
        model = m.Product
        fields = "__all__"

    def get_new(self, obj):
        delta = now().date() - obj.created

        if delta.days < 30:
            return True
        return False
    
    def get_image(self, obj):
        return obj.image.url

class CategorySerializer(ReadOnlyModelSerializer):

    class Meta:
        model = m.Category
        fields = "__all__"

class SizeSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = m.Size
        fields = "__all__"

class ColourSerializer(ReadOnlyModelSerializer):

    class Meta:
        model = m.Colour
        fields = "__all__"
