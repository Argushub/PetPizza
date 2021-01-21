from django.db import models


class ProductType(models.Model):
    """
    This model representing product type such as table, food, fridge, etc.
    """
    type_name = models.CharField(max_length=20, help_text="Enter a product type name")
    image = models.ImageField(default=None)

    class Meta:
        ordering = ['type_name']

    def __str__(self):
        return self.type_name
