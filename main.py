from pokemon import Pokemon
from get_database_scrap import get_database_scrap

pokemon = input("Enter a pokemon's name: ").lower().strip()

database_scrap = get_database_scrap('https://pokemondb.net/pokedex/' + pokemon)

print(database_scrap)