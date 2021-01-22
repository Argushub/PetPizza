from django.db import models
from .pizza import Pizza
from ...customer import Customer


class PizzaInstance(models.Model):
    """
    This model representing instance of pizza, that was be bought.
    """
    order_time = models.DateTimeField()
    pizza_type = models.ForeignKey(
        Pizza,
        on_delete=models.SET_NULL,
        null=True
    )
    DOUGH_TYPE = (
        ('tr', 'traditional'),
        ('th', 'thin')
    )
    dough = models.CharField(max_length=2, choices=DOUGH_TYPE, help_text='Dough type')
    SIZE_TYPE = (
        ('25', '25 sm'),
        ('30', '30 sm'),
        ('35', '35 sm'),
        ('40', '40 sm')
    )
    size = models.CharField(max_length=2, choices=SIZE_TYPE, help_text='Pizza size')
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        ordering = ['order_time']

    def __str__(self):
        return "{}: {}, {}".format(self.order_time, self.pizza_type.type.name, self.pizza_type.name)
