from django.shortcuts import render
from ..models import Snack


def snack(request):
    """
    Func display all snacks
    """
    snacks = Snack.objects.all()

    return render(
        request,
        'snack.html',
        context={'snacks': snacks}
    )
