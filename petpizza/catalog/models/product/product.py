from django.db import models
from ..product_type import ProductType


class Product(models.Model):
    """
    This model representing product such as iPhone 11, Coca Cola Vanilla, etc.
    """
    name = models.CharField(max_length=50, default=None, help_text="Enter a product name")
    price = models.IntegerField(default=None, help_text="Enter a price")
    type = models.ForeignKey(ProductType,
                             null=True,
                             on_delete=models.SET_NULL,
                             help_text="Select a product type",
                             )
    description = models.TextField(max_length=1000, default=None, help_text="Enter a description of the product")
    image = models.ImageField(default=None)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name