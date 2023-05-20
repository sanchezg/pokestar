from rest_framework.filters import BaseFilterBackend


class PokemonFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        values = request.query_params.get(self.field)
        if not values:
            return queryset

        values = values.split(",")
        for v in values:
            queryset = queryset.filter(**{self.query_lookup: v})
        return queryset


class PokemonMovesFilterBackend(PokemonFilterBackend):
    field = "moves"
    query_lookup = "moves__name"


class PokemonTypesFilterBackend(PokemonFilterBackend):
    field = "types"
    query_lookup = "types__name"
