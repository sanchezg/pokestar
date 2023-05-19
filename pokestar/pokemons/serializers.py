from rest_framework import serializers

from .models import Pokemon, PokemonMove, PokemonType


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"


class PokemonMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonMove
        fields = "__all__"


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = "__all__"
