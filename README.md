# POKEDEX
A simple attempt to create a pokedex like script using webscraping techniques and pokemondb.net data

## Features
Fetch pokemon stats data from https://pokemondb.net and uses provided data to instantiate pokemon objects from the Pokemon class.

## Pokemon stats
For now, you can get the following attributes from the pokemon class:
- Pokemon.name
- Pokemon.hp
- Pokemon.attack
- Pokemon.defense
- Pokemon.sp_attack
- Pokemon.sp_defense
- Pokemon.speed

## Installing and running

- Install python dependencies

  > pip install bs4 requests
  
- Clone this repository

  > git clone https://github.com/yagolimalins/pokedex.git
  
- Run the main.py file

  > python ./pokedex/main.py
