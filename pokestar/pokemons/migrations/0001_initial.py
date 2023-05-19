# Generated by Django 4.2.1 on 2023-05-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PokemonMove",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("power", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="PokemonType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Pokemon",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("order", models.IntegerField()),
                ("height", models.IntegerField()),
                ("weight", models.IntegerField()),
                ("moves", models.ManyToManyField(to="pokemons.pokemonmove")),
                ("types", models.ManyToManyField(to="pokemons.pokemontype")),
            ],
        ),
    ]
