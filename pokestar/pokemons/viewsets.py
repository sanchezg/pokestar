from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import PokemonMovesFilterBackend, PokemonTypesFilterBackend
from .models import Pokemon, PokemonMove, PokemonType
from .serializers import PokemonMoveSerializer, PokemonSerializer, PokemonTypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = []
    filter_backends = [PokemonMovesFilterBackend, PokemonTypesFilterBackend]

    @action(detail=True)
    def best_move(self, request, pk=None):
        pokemon: Pokemon = self.get_object()
        if pokemon.moves.exists():
            serializer = PokemonMoveSerializer(pokemon.moves.order_by("-power").first())
            return Response(serializer.data)
        return Response()


class PokemonMoveViewSet(viewsets.ModelViewSet):
    queryset = PokemonMove.objects.all()
    serializer_class = PokemonMoveSerializer
    permission_classes = []


class PokemonTypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = PokemonTypeSerializer
    permission_classes = []
