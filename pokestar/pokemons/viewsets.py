from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets

from .filters import PokemonMovesFilterBackend, PokemonTypesFilterBackend
from .models import Pokemon, PokemonMove, PokemonType
from .serializers import PokemonMoveSerializer, PokemonSerializer, PokemonTypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = []
    filter_backends = [PokemonMovesFilterBackend, PokemonTypesFilterBackend]


class PokemonMoveViewSet(viewsets.ModelViewSet):
    queryset = PokemonMove.objects.all()
    serializer_class = PokemonMoveSerializer
    permission_classes = []


class PokemonTypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = PokemonTypeSerializer
    permission_classes = []
