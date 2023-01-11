from pokemon import Pokemon
from get_database_scrap import get_database_scrap

active = True

while active:

    pokemon_input = input("Enter a pokemon's name: ").lower().strip()

    database_scrap = get_database_scrap('https://pokemondb.net/pokedex/' + pokemon_input)

    pokemon = Pokemon(pokemon_input, database_scrap)

    print(pokemon.name.upper() + " POKEDEX DATA:")
    print("HP: " + pokemon.hp +
          "\nAttack: " + pokemon.attack +
          "\nDefense: " + pokemon.defense +
          "\nSP Attack: " + pokemon.sp_attack +
          "\nSP Defense: " + pokemon.sp_defense +
          "\nSpeed: " + pokemon.speed)