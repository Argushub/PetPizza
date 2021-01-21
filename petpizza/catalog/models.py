from django.db import models


class Customer(models.Model):
    telephone_number = models.CharField(max_length=12, primary_key=True)
    address = models.CharField(max_length=30)


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


class Pizza(Product):
    """
    This model representing pizza as is.
    """
    consist = models.TextField(max_length=500, help_text="Enter pizza consist")


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
        return "{}: {}".format(self.order_time, self.pizza_type.name)
