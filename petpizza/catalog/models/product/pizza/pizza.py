from django.db import models
from ..product import Product


class Pizza(Product):
    """
    This model representing pizza as is.
    """
    consist = models.TextField(max_length=500, help_text="Enter pizza consist")
