from functions.db_scrap import db_scrap
from pokemon import Pokemon

active = True

while active:
    print("----------------------")

    pokemon_input = input("Enter a pokemon's name: ")

    pokedex_data = db_scrap(pokemon_input)

    pokemon = Pokemon(pokemon_input)

    pokemon.show_data()
