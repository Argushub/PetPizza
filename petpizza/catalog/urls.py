from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('pizza', views.pizza, name='pizza'),
    path('drink', views.drink, name='drink'),
    path('snack', views.snack, name='snack')
]

