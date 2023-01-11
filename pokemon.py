from get_base_stats import get_base_stats

class Pokemon:
    """Design a pokemon's stats tree using methods fed by scrapping data"""
    def __init__(self, name, pokedex_scrap):

        base_stats = get_base_stats(pokedex_scrap)

        self.name = name
        self.hp = base_stats['hp']
        self.attack = base_stats['attack']
        self.defense = base_stats['defense']
        self.sp_attack = base_stats['sp_attack']
        self.sp_defense = base_stats['sp_defense']
        self.speed = base_stats['speed']