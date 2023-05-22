from typing import List

import click
import requests

from pokestar.pokemons.pokeapi import PokeApiFetcher

BASE_URL = "http://localhost:8000/api/v1/pokemons/"


@click.group()
def apifetcher():
    pass


@apifetcher.command()
@click.option("--type", "-t", multiple=True)
def by_type(type: List[str]):
    types = ",".join(type)
    result = requests.get(BASE_URL, data={"types": types})
    data = result.json()
    print(f"I have found {data['count']} Pokemons with types '{types}'. These are the names for the first 20:")
    print([x["name"] for x in data["results"]])


@apifetcher.command()
@click.option("--move", "-m", multiple=True)
def by_move(move: List[str]):
    moves = ",".join(move)
    result = requests.get(BASE_URL, data={"moves": moves})
    data = result.json()
    print(f"I have found {data['count']} Pokemons with moves '{moves}'. These are the names for the first 20:")
    print([x["name"] for x in data["results"]])


@apifetcher.command()
def fetch_pokemons():
    amount = 10
    po = PokeApiFetcher(limit=amount)
    purls, next_url = po.get_pokemons_urls_list()
    print(f"Getting {amount} pokemons from PokeAPI ...")
    pokemons = []
    for url_info in purls:
        print(f"Getting info for {url_info['name']} ...")
        pokemons.append(po.make_pokemon_by_url(url_info["url"]))

    print(pokemons)


if __name__ == "__main__":
    apifetcher()
