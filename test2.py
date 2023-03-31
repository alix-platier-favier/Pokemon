import sys
import time
import random

#delay print
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, types, moves, EVs):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs["ATTACK"]
        self.defense = EVs["DEFENSE"]
        self.health = 100
        self.s1_attack = None
        self.s2_attack = None


    def attack_def(self, pokemon2):
        version = ["Fire", "Water", "Grass"]
        for i, k in enumerate(version):
            if self.types == k:
                if pokemon2.types == k:
                    self.s1_attack = "It's not very effective..."
                    self.s2_attack = "It's not very effective..."

                if pokemon2.types == version[(i+1)%3]:
                    pokemon2.attack *= 2
                    pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /=2
                    self.s1_attack = "It's not very effective..."
                    self.s2_attack = "It's super effective!"

                if pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    pokemon2.attack /= 2
                    pokemon2.defense /=2
                    self.s1_attack = "It's super effective!"
                    self.s2_attack = "It's not very effective..."


    def fight(self, pokemon2):
        print("------POKEMON FIGHTING------")
        print(f"\n{self.name}")
        print("TYPE:", self.types)
        print("ATTACK:", self.attack)
        print("DEFENSE:", self.defense)
        print("LVL:", 1)
        print("\nVS")
        print(f"\n{pokemon2.name}")
        print("TYPE:", pokemon2.types)
        print("ATTACK:", pokemon2.attack)
        print("DEFENSE:", pokemon2.defense)
        print("LVL:", 1)

        time.sleep(2)

        while (self.health > 0) and (pokemon2.health > 0):
                    print(f"\n{self.name}\t\tHealth:\t{self.health}")
                    print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}")        
                    print(f"\nGO {self.name}!")
                    
                    for i, x in enumerate(self.moves):
                        print(f"{i+1}.", x)
                        index = int(input("\nPick a move: "))
                        
                        delay_print(f"{self.name} used {self.moves[index-1]}\n")
                        time.sleep(2)
                        delay_print(self.s1_attack)

                    pokemon2.health -= self.attack
                    pokemon2.health = ""
                    
                    for j in range(pokemon2.health+.1*pokemon2.defense):
                        pokemon2.health += ""

                    time.sleep(2)

                    print(f"\n{self.name}\t\tHealth:\t{self.health}")
                    print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}") 
                    time.sleep(1)

                    if pokemon2.health <= 0:
                        delay_print("\n..." + pokemon2.name + "Fainted. \nYOU WIN!")
                        break

                    print(f"GO {pokemon2.name}!")
                        
                    for i, x in enumerate(pokemon2.moves):
                        print(f"{i+1}.", x)
                        index = int(input("\nPick a move: "))
                        delay_print(f"{pokemon2.name} used {pokemon2.moves[index-1]}\n")
                        time.sleep(2)
                        delay_print(self.s2_attack)

                    pokemon2.health -= self.attack
                    pokemon2.health = ""
                    
                    for j in range(pokemon2.health+.1*pokemon2.defense):
                        pokemon2.health += ""


                    time.sleep(2)

                    print(f"\n{self.name}\t\tHealth:\t{self.health}")
                    print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}") 
                    time.sleep(1)

                    if self.health <= 0:
                        delay_print("\n..." + self.name + "Fainted. \nYou lose...")


if __name__ == '__main__':
    Charizard = Pokemon("Charizard", "Fire", ["Flamethrower", "Fly", "Blast", "Fire Punch"], {"ATTACK": 12, "DEFENSE": 8})
    Blastoise = Pokemon("Blastoise", "Water", ["Water Gun", "Fly", "Blast", "Fire Punch"], {"ATTACK": 12, "DEFENSE": 8})
    Venusaur = Pokemon("Venusaur", "Grass", ["Vine wip", "Fly", "Blast", "Fire Punch"], {"ATTACK": 12, "DEFENSE": 8})

Charizard.fight(Venusaur)
                  