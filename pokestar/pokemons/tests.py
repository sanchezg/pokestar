from django.test import TestCase
from rest_framework.test import APIClient

BASE_PATH = "/api/v1"


class PokemonViewSetTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.path = f"{BASE_PATH}/pokemons/"
        return super().setUp()

    def test_pokemon_viewset_get_all_includes_moves(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

    def test_pokemon_viewset_get_can_filter_per_type(self):
        pass

    def test_pokemon_viewset_get_can_filter_per_move(self):
        pass
