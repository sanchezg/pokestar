# Generated by Django 4.2.1 on 2023-05-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="created_at",
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name="pokemon",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="height",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="name",
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="order",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="weight",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
