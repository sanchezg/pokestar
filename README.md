# PokeStar: A Pokemons fetcher

Developed as assessment for an interview, this project was entirely developed using Python 3.10, Django, rest-framework, Celery, RabbitMQ, and Postgres.

## Running instructions

Preferred way is to run it using docker:

```
docker-compose -f docker/docker-compose.yml build
docker-compose -f docker/docker-compose.yml up
```

You can also install all infra dependencies on your side and run it by hand with Poetry:

```
poetry install
poetry run python manage.py runserver 0.0.0.0:8000
```

In both ways, hitting `http://localhost:8000/pokemons/` should show you an HTML web with the latest 5 pokemons retrieved from PokeAPI.
In that HTML page, there's a submit form button to retrieve pokemons from PokeAPI. If you hit it, check the broker and worker container logs to see if the tasks are running in background.

## Testing the API with a client

A CLI client was included in `pokefetcher/apifetcher.py` with two functions:

1. Fetching Pokemons from PokeAPI: run the cli client with `python apifetcher.py fetch-pokemons`
2. Filtering Pokemons from local API: run the cli client with `python apifetcher.py by-move -m MOVE1 -m MOVE2 ...` or `python apifetcher.py by-type -t TYPE1 -t TYPE2 ...` to filter Pokemons stored locally.
