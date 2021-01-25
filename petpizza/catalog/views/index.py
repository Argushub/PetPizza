from django.shortcuts import render
from ..models import Pizza, Drink, Snack


def index(request):
    """
    Func display main page with all products
    """
    pizzas = Pizza.objects.all()
    drinks = Drink.objects.all()
    snacks = Snack.objects.all()

    return render(
        request,
        'index.html',
        context={'pizzas': pizzas, 'drinks': drinks, 'snacks': snacks}
    )
