from django.db import models


class Product(models.Model):
    """
    This is abstract model for product.
    """
    name = models.CharField(max_length=50, default=None, help_text="Enter a product name")
    price = models.IntegerField(default=None, help_text="Enter a price")
    description = models.TextField(max_length=1000, default=None, help_text="Enter a description of the product")
    image = models.ImageField(default=None)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name
