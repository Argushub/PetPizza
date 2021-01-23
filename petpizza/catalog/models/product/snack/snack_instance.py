from django.db import models
from .snack import Snack
from ..product_instance import ProductInstance


class SnackInstance(ProductInstance):
    order_time = models.DateTimeField()
    snack_type = models.ForeignKey(
        Snack,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return "{}: {}, {}".format(self.order_time, self.snack_type.name, self.snack_type.number)
