from django.contrib import admin

from .models import Pokemon, PokemonMove, PokemonType


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
        "height",
        "weight",
    )


admin.site.register(PokemonMove)
admin.site.register(PokemonType)
