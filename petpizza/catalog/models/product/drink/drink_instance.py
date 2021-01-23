from django.db import models
from .drink import Drink
from ..product_instance import ProductInstance


class DrinkInstance(ProductInstance):
    order_time = models.DateTimeField()
    drink_type = models.ForeignKey(
        Drink,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return "{}: {}, {}".format(self.order_time, self.drink_type.name, self.drink_type.volume)
