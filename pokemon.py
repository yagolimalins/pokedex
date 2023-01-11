from functions.get_pokedex_data import get_pokedex_data
from functions.get_base_stats import get_base_stats
from functions.db_scrap import db_scrap


class Pokemon:
    """Design a pokemon's stats and data tree using methods fed by scrapping data"""

    def __init__(self, name):
        html = db_scrap(name)

        pokedex_data = get_pokedex_data(html)

        self.name = name.title()

        self.number = pokedex_data['number']
        self.type = pokedex_data['type']
        self.species = pokedex_data['species']
        self.height = pokedex_data['height']
        self.weight = pokedex_data['weight']
        # self.abilities = pokedex_data['abilities']
        # self.local = pokedex_data['local']

        base_stats = get_base_stats(html)

        self.hp = base_stats['hp']
        self.attack = base_stats['attack']
        self.defense = base_stats['defense']
        self.sp_attack = base_stats['sp_attack']
        self.sp_defense = base_stats['sp_defense']
        self.speed = base_stats['speed']

    def show_data(self):
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)
