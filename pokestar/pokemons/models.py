from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class PokemonMove(models.Model):
    name = models.CharField(max_length=255)
    power = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    order = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    types = models.ManyToManyField(PokemonType)
    moves = models.ManyToManyField(PokemonMove)

    def __str__(self) -> str:
        return self.name
