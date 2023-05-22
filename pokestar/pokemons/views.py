from django.shortcuts import render

from .models import Pokemon
from .tasks import fetch_pokemons_list


def index(request):
    if request.method == "POST":
        fetch_pokemons_list.delay()
    pokemons = Pokemon.objects.order_by("-created_at")[:5]
    context = {
        "pokemons_list": pokemons,
    }
    return render(request, "index.html", context)
