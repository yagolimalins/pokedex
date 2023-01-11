from pokemon import Pokemon

active = True

while active:
    print("----------------------")

    pokemon_input = input("Enter a pokemon's name: ")

    pokemon = Pokemon(pokemon_input)

    pokemon.show_data()
