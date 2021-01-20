from django.db import models


class ProductType(models.Model):
    """
    This model representing product type such as table, food, fridge, etc.
    """
    type_name = models.CharField(max_length=20, help_text="Enter a product type name")
    id = models.IntegerField(max_length=5, primary_key=True)

    class Meta:
        ordering = ['type_name']

    def __str__(self):
        return self.type_name


class Product(models.Model):
    """
    This model representing product such as iPhone 11, Coca Cola Vanilla, etc.
    """
    name = models.CharField(max_length=50, help_text="Enter a product name")
    price = models.IntegerField(max_length=6, help_text="Enter a price")
    type = models.ManyToManyField(ProductType, help_text="Select a product type")
    description = models.CharField(max_length=200, help_text="Enter a description of the product")
