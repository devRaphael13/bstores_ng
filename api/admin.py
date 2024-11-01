from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models as m

@admin.register(m.Product)
class Product(ModelAdmin):
    pass

@admin.register(m.Category)
class Category(ModelAdmin):
    pass

@admin.register(m.Size)
class Size(ModelAdmin):
    pass

@admin.register(m.Colour)
class Colour(ModelAdmin):
    pass
