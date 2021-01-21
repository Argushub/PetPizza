from django.contrib import admin
from .models.customer import Customer
from .models.product_type import ProductType
from .models.product.pizza.pizza import Pizza
from .models.product.pizza.pizza_instance import PizzaInstance


admin.site.register(Customer)
admin.site.register(ProductType)
admin.site.register(Pizza)
admin.site.register(PizzaInstance)
