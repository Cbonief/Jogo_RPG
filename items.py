import numpy as np


class Weapon:
    def __init__(self, name, attack_range, base_damage, damage_multiplier=None):
        self.name = name
        self.range = attack_range                           # Int: 1 to 10. If 1, it's a melee weapon.
        self.base_damage = base_damage                      # 2D Int vectotr [number_of_die, dice_value]
        self.damage_multiplier = damage_multiplier          # Dictionary; {'Attribute': [], 'Multiplier': []}

    def get_damage(self):
        damage = 0
        dice_value = self.base_damage[1]
        for dice in range(0, self.base_damage[0]):
            roll = dice_value
            while roll == dice_value:
                roll = np.random.randint(1, high=dice_value+1)
                damage += roll
        return damage
        # for [attribute, multiplier] in zip(self.damage_multiplier['Attribute'], self.damage_multiplier['Multiplier']):


sword = Weapon('Sword', 1, [2, 4])
bow = Weapon('Bow', 4, [1, 8])
