from django.db import models
from ..customer import Customer


class ProductInstance(models.Model):
    """
    This is abstract model for instance of product.
    """
    order_time = models.DateTimeField()
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        abstract = True
        ordering = ['order_time']
