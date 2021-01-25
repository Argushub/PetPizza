from django.shortcuts import render
from ..models import Drink


def drink(request):
    """
    Func display all drinks
    """
    drinks = Drink.objects.all()

    return render(
        request,
        'drink.html',
        context={'drinks': drinks}
    )
