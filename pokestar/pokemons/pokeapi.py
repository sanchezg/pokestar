from dataclasses import dataclass
from typing import List, Optional

import requests

BASE_URL = "https://pokeapi.co/api/v2/"
POKEMON_RESOURCE = "pokemon/"
MOVES_RESOURCE = "move/"


@dataclass
class PokemonType:
    name: str


@dataclass
class PokemonMove:
    name: str
    power: int


@dataclass
class Pokemon:
    name: str
    order: int
    height: int
    weight: int
    types: Optional[List[PokemonType]] = None
    moves: Optional[List[PokemonMove]] = None


class PokeApiFetcher:
    def __init__(self, base_url: str = BASE_URL, limit: int = 500) -> None:
        self.session = requests.Session()
        self.base_url = base_url
        self.limit = limit

    @property
    def pokemons_url(self) -> str:
        return f"{self.base_url}{POKEMON_RESOURCE}"

    @property
    def moves_url(self) -> str:
        return f"{self.base_url}{MOVES_RESOURCE}"

    def get_pokemons_urls_list(self, offset: int = None, url: str = None):
        params = {"limit": self.limit}
        if offset is not None:
            params["offset"] = offset

        url = url or self.pokemons_url
        response = self.session.get(url, params=params)
        data = response.json()

        return data.get("results", []), data.get("next")

    def make_pokemon_by_url(self, url: str) -> Optional[Pokemon]:
        response = self.session.get(url)
        pokemon_data = response.json()

        if not pokemon_data:
            return None

        pokemon = Pokemon(
            name=pokemon_data["name"],
            order=pokemon_data["order"],
            height=pokemon_data["height"],
            weight=pokemon_data["weight"],
        )

        _moves = []
        for move_data in pokemon_data["moves"]:
            move = self.get_pokemon_move_by_url(move_data["move"]["url"])
            if move:
                _moves.append(move)
        if _moves:
            pokemon.moves = _moves

        _types = []
        for type_data in pokemon_data["types"]:
            _types.append(PokemonType(name=type_data["type"]["name"]))
        if _types:
            pokemon.types = _types

        return pokemon

    def get_pokemon_move_by_url(self, url: str):
        response = self.session.get(url)
        data = response.json()
        if data:
            return PokemonMove(name=data["name"], power=data["power"])
        return None
