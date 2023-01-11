from get_base_stats import get_base_stats

class Pokemon:
    """Basic class for a pokemon's base stats"""
    def __init__(self, name):

        base_stats = get_base_stats()

        self.name = name
        self.hp = base_stats[0][0]
        self.attack = base_stats[1][0]
        self.defense = base_stats[2][0]
        self.sp_attack = base_stats[3][0]
        self.sp_defense = base_stats[4][0]
        self.speed = base_stats[5][0]