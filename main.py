from pokemon import Pokemon
from db_scrap import pokedex_scrap
from print_pokemon_data import print_pokemon_data

active = True

while active:
    print("----------------------")

    pokemon_input = input("Enter a pokemon's name: ")

    pokedex_data = pokedex_scrap(pokemon_input)

    pokemon = Pokemon(pokemon_input, pokedex_data)

    print_pokemon_data(pokemon)