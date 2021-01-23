from django.contrib import admin
from .models.customer import Customer
from .models.product.product_order import ProductOrder
from .models.product.pizza import Pizza
from .models.product.snack import Snack
from .models.product.drink import Drink
from .models.product.product import Product


admin.site.register(Customer)
admin.site.register(Pizza)
admin.site.register(Drink)
admin.site.register(Snack)
admin.site.register(Product)
admin.site.register(ProductOrder)
