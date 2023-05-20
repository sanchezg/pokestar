from django.test import TestCase
from rest_framework.test import APIClient

from .factories import PokemonFactory, PokemonMoveFactory, PokemonTypeFactory

BASE_PATH = "/api/v1"


class PokemonViewSetTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.path = f"{BASE_PATH}/pokemons/"
        return super().setUp()

    def test_pokemon_viewset_GET_all_includes_moves(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

    def test_pokemon_viewset_GET_can_filter_per_type(self):
        PokemonFactory(types=(PokemonTypeFactory(name="type1"), PokemonTypeFactory(name="type2")))
        PokemonFactory(types=(PokemonTypeFactory(name="type1"),))

        response = self.client.get(self.path, data={"types": "type1"})

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 2)

        response = self.client.get(self.path, data={"types": "type2"})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 1)

    def test_pokemon_viewset_GET_can_filter_per_move(self):
        PokemonFactory(moves=(PokemonMoveFactory(name="move1"), PokemonMoveFactory(name="move2")))
        PokemonFactory(moves=(PokemonMoveFactory(name="move1"),))

        response = self.client.get(self.path, data={"moves": "move1"})

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 2)

        response = self.client.get(self.path, data={"moves": "move2"})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 1)

    def test_pokemon_viewset_GET_filters_per_types_includes_all(self):
        PokemonFactory(types=(PokemonTypeFactory(name="type1"), PokemonTypeFactory(name="type2")))
        PokemonFactory(types=(PokemonTypeFactory(name="type1"),))

        response = self.client.get(self.path, data={"types": "type1,type2"})

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 1)  # only result that has both types

    def test_pokemon_viewset_GET_filters_per_moves_includes_all(self):
        PokemonFactory(moves=(PokemonMoveFactory(name="move1"), PokemonMoveFactory(name="move2")))
        PokemonFactory(moves=(PokemonMoveFactory(name="move1"),))

        response = self.client.get(self.path, data={"moves": "move1,move2"})

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 1)
