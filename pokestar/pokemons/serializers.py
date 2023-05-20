from rest_framework import serializers

from .models import Pokemon, PokemonMove, PokemonType


class PokemonMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonMove
        fields = (
            "name",
            "power",
        )


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = ("name",)


class PokemonSerializer(serializers.ModelSerializer):
    types = PokemonTypeSerializer(many=True, read_only=True)
    moves = PokemonMoveSerializer(many=True, read_only=True)

    class Meta:
        model = Pokemon
        fields = (
            "name",
            "order",
            "height",
            "weight",
            "types",
            "moves",
        )
