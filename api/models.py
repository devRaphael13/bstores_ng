from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

class Product(models.Model):
    image = CloudinaryField("product_image")
    name = models.CharField(max_length=120)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    sizes = models.ManyToManyField("Size", blank=True)
    colours = models.ManyToManyField("Colour", blank=True)
    featured = models.BooleanField(default=False)
    num_of_customers = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Size(models.Model):
    size = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.size

@receiver(pre_save, sender=Size)
def to_uppercase(sender, instance, **kwargs):
    instance.size = instance.size.upper()

@receiver(pre_save, sender=Colour)
def to_uppercase(sender, instance, **kwargs):
    instance.name = instance.name.upper()
