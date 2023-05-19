from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import PokemonMoveViewSet, PokemonTypeViewSet, PokemonViewSet

app_name = "pokemons"

router = DefaultRouter()
router.register(r"pokemons", PokemonViewSet)
router.register(r"pokemonmoves", PokemonMoveViewSet)
router.register(r"pokemontypes", PokemonTypeViewSet)
