import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        # TODO: Element based damage calculation
        dmgh = self.dmg + 5
        dmgl = self.dmg - 5
        return random.randrange(dmgl, dmgh)

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost
    

