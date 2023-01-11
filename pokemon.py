from get_base_stats import get_base_stats

class Pokemon:
    """Design a pokemon's stats tree using methods fed by scrapping data"""
    def __init__(self, name, database_scrap):

        base_stats = get_base_stats(database_scrap)

        self.name = name
        self.hp = base_stats[0][0]
        self.attack = base_stats[1][0]
        self.defense = base_stats[2][0]
        self.sp_attack = base_stats[3][0]
        self.sp_defense = base_stats[4][0]
        self.speed = base_stats[5][0]