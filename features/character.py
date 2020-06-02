import random


class Character:
    def __init__(self, hp, mana, armor, mr, atk, spells):
        self.hp = hp
        self.max_hp = hp
        self.mana = mana
        self.max_mana = mana
        self.armor = armor
        self.mr = mr
        self.atkl = atk - 5
        self.atkh = atk + 5
        self.spells = spells
        self.actions = ["Normal Attack", "Spell"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.max_hp
    
    def get_mana(self):
        return self.mana
    
    def get_max_mana(self):
        return self.max_mana

    def decrease_mana(self, cost):
        self.mana -= cost

    def choose_action(self):
        index = 1
        print("Actions")
        for action in self.actions:
            print(str(index) + ". " + action)
            index += 1
    
    def choose_spell(self):
        index = 1
        print("Spells")
        for spell in self.spells:
            print(str(index) + ". " + spell.name + " (Mana Cost: "  +  str(spell.cost) + ")")
            index += 1
    




