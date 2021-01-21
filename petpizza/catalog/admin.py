from django.contrib import admin
from .models import Customer, ProductType, Pizza, PizzaInstance


admin.site.register(Customer)
admin.site.register(ProductType)
admin.site.register(Pizza)
admin.site.register(PizzaInstance)