from django.db import models
from .product import Product


class Drink(Product):
    volume = models.CharField(max_length=20, help_text="Enter the volume of drink")
