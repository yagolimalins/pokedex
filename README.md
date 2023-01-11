# POKEDEX
A simple attempt to create a Pokedex like script using webscraping techniques and pokemondb.net data

## Features
Provides a Pokemon class capable of fetching pokemon data from https://pokemondb.net upon class instantiation and make this data available through attributes

## Installing and running

- Install python dependencies

  > pip install bs4 requests
  
- Clone this repository

  > git clone https://github.com/yagolimalins/pokedex.git
  
- Run the main.py file

  > python ./pokedex/main.py

## Usage as a simple Pokedex
Running the main.py file and providing the input prompt a pokemon's name (ex: pikachu) will return

    Enter a pokemon's name: pikachu
    name = Pikachu
    number = 025
    type = Electric
    species = Mouse Pokémon
    height = 0.4 m (1′04″)
    weight = 6.0 kg (13.2 lbs)
    hp = 35
    attack = 55
    defense = 40
    sp_attack = 50
    sp_defense = 50
    speed = 90

## Usage as a module inside your own python code
Imoporting the pokemon.py module content and creating a instance of the Pokemon class will create a Pokemon object with his respective attributes, for example:

    pokemon = Pokemon('pikachu')
    print(pokemon.species)

Will instantiate a pokemon object with and fetch all related data to this pokemon, afterward the print statement will return the *species* attribute from this object, the print message will show:

    Mouse Pokémon

Check the available class attributes below

## Pokemon Attributes
For now, you can get the following attributes from the pokemon class:

- Pokemon.name
- Pokemon.number
- Pokemon.type
- Pokemon.species
- Pokemon.height
- Pokemon.weight
- Pokemon.hp
- Pokemon.attack
- Pokemon.defense
- Pokemon.sp_attack
- Pokemon.sp_defense
- Pokemon.speed
