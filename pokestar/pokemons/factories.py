import random

import factory
from factory.django import DjangoModelFactory

from .models import Pokemon, PokemonMove, PokemonType


class PokemonMoveFactory(DjangoModelFactory):
    class Meta:
        model = PokemonMove
        django_get_or_create = ("name",)

    name = factory.LazyFunction(lambda: random.choice(["substitute", "swagger", "giga-drain", "petal-dance"]))
    power = factory.LazyFunction(lambda: random.randint(1, 100))


class PokemonTypeFactory(DjangoModelFactory):
    class Meta:
        model = PokemonType
        django_get_or_create = ("name",)

    name = random.choice(["grass", "poison", "fire", "water"])


class PokemonFactory(DjangoModelFactory):
    class Meta:
        model = Pokemon

    name = factory.Faker("first_name")
    order = factory.LazyFunction(lambda: random.randint(1, 100))
    weight = factory.LazyFunction(lambda: random.randint(1, 100))
    height = factory.LazyFunction(lambda: random.randint(1, 100))

    @factory.post_generation
    def moves(self, create, extracted, **kwargs):
        if not create and not extracted:
            return

        if extracted:
            self.moves.add(*extracted)
            return

        self.moves.add(PokemonMoveFactory())

    @factory.post_generation
    def types(self, create, extracted, **kwargs):
        if not create and not extracted:
            return

        if extracted:
            self.types.add(*extracted)
            return

        self.types.add(PokemonTypeFactory())
