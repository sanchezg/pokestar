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
