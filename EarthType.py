from Pokemon import Pokemon

class Earth(Pokemon):
    def __init__(self, name, lvl, pa):
        super().__init__(name, lvl, pa)

    def __str__(self):
        return f'Name: {self.__name},\nPV: {self.__pv},\n Attack: {self.pa},\n Defense: {self.defense}'