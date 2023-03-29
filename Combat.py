from Pokemon import Pokemon
from EarthType import Earth
from WaterType import Water
from FireType import Fire
from NormalType import Normal

class Combat(Pokemon):
    def __init__(self, name, lvl, pa, pokemon1, pokemon2, water, earth, fire, normal):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.water = water
        self.normal = normal
        self.fire = fire
        self.earth = earth

    def check_pv(self):
        pass

    def check_winner(self):
        pass

    def check_loser(self):
        pass

    def attack_defense(self):
        pass

    def remove_pv_def(self):
        board = {
    "Water": {"Water": 1, "Fire": 2, "Earth": 0.5, "Normal": 1},
    "Fire": {"Water": 0.5, "Fire": 1, "Earth": 2, "Normal": 1},
    "Earth": {"Water": 2, "Fire": 0.5, "Earth": 1, "Normal": 1},
    "Normal": {"Water": 0.75, "Fire": 0.75, "Earth": 0.75, "Normal": 1}
}
        i = 

    def start_game(self):
        pass
