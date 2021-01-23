from django.db import models
from .product import Product
from ..customer import Customer


class ProductOrder(models.Model):
    """
    This is abstract model for instance of product.
    """
    order_time = models.DateTimeField()

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True
    )

    PRODUCT_TYPE = (
        ('1', 'pizza'),
        ('2', 'snack'),
        ('3', 'drink')
    )

    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE)

    # I'm using polymorphic django for better model inheritance
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )

    # size is universal field for all type of product size
    size = models.CharField(max_length=20, default=None, null=True)

    class Meta:
        ordering = ['order_time']

    def __str__(self):
        return "{}:{} {}".format(self.order_time, self.product.name, self.size)
