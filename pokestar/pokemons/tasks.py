from celery import shared_task

from .models import Pokemon
from .pokeapi import PokeApiFetcher


@shared_task
def fetch_pokemon(pokemon_url):
    handler = PokeApiFetcher()
    pdatac = handler.make_pokemon_by_url(pokemon_url)
    Pokemon.from_dataclass(pdatac)


@shared_task
def fetch_pokemons_list():
    handler = PokeApiFetcher()
    purls, next_url = handler.get_pokemons_urls_list()
    for url_info in purls:
        fetch_pokemon.delay(url_info["url"])
