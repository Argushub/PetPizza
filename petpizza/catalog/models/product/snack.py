from django.db import models
from .product import Product


class Snack(Product):
    """
    This class representing snacks e.g. Lays, nuggets, etc.
    """
    consist = models.CharField(max_length=500)
    number = models.CharField(max_length=30, help_text="Enter amount or weight")
