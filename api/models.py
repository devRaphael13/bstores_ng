from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    image = CloudinaryField("product_image")
    name = models.CharField(max_length=120)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    sizes = models.JSONField(default=list)
    colors = models.JSONField(default=list)

class Category(models.Model):
    name = models.CharField(max_length=40)
