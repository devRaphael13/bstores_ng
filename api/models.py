from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    image = CloudinaryField("product_image")
    name = models.CharField(max_length=120)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    sizes = models.JSONField(default=list)
    colors = models.JSONField(default=list)
    featured = models.BooleanField(default=False)
    num_of_customers = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
