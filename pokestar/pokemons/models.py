from dataclasses import asdict

from django.db import models

from .pokeapi import Pokemon as PokemonDC


class PokemonType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class PokemonMove(models.Model):
    name = models.CharField(max_length=255)
    power = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    order = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    types = models.ManyToManyField(PokemonType)
    moves = models.ManyToManyField(PokemonMove)

    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_dataclass(obj: PokemonDC):
        data = asdict(obj)
        _moves = data.pop("moves", [])
        _types = data.pop("types", [])

        pobj = Pokemon.objects.create(**data)
        for move in _moves:
            mobj, created = PokemonMove.objects.get_or_create(name=move["name"], power=move["power"])
            pobj.moves.add(mobj)

        for type in _types:
            tobj, created = PokemonType.objects.get_or_create(name=type["name"])
            pobj.types.add(tobj)
        pobj.save()

        return pobj
