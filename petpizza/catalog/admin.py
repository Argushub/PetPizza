from django.contrib import admin
from .models.customer import Customer
from .models.product.pizza.pizza import Pizza
from .models.product.pizza.pizza_instance import PizzaInstance
from .models.product.snack.snack import Snack
from .models.product.snack.snack_instance import SnackInstance
from .models.product.drink.drink import Drink
from .models.product.drink.drink_instance import DrinkInstance


admin.site.register(Customer)
admin.site.register(Pizza)
admin.site.register(PizzaInstance)
admin.site.register(Drink)
admin.site.register(DrinkInstance)
admin.site.register(Snack)
admin.site.register(SnackInstance)
