from django.shortcuts import render
from ..models import Pizza


def pizza(request):
    """
    Func display all pizzas
    """
    pizzas = Pizza.objects.all()

    return render(
        request,
        'pizza.html',
        context={'pizzas': pizzas}
    )
