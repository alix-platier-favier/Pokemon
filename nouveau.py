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
    def __init__(self, name, types, moves, EVs, health):
        self.name = name
        self.types = types
        self.moves = moves
        self.move_name = None
        self.attack = EVs["ATTACK"]
        self.defense = EVs["DEFENSE"]
        self.health = health
        self.s1_attack = None
        self.s2_attack = None
        self.max_health = 100

    def reset(self):
        self.health = self.max_health

    def attack_def(self, pokemon2):
        version = ["Fire", "Water", "Earth", "Normal"]
        for i, k in enumerate(version):
            if self.types == k:
                if pokemon2.types == k:
                    print("It's not very effective...")
                    print("It's not very effective...")

                elif pokemon2.types == version[(i+1)%4]:
                    pokemon2.attack *= 2
                    pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /=2
                    print("It's not very effective...")
                    print("It's super effective!")

                elif pokemon2.types == version[(i+2)%4]:
                    self.attack *= 2
                    self.defense *= 2
                    pokemon2.attack /= 2
                    pokemon2.defense /=2
                    print("It's super effective!")
                    print("It's not very effective...")

        print(f"\n{self.name}\t\tHealth:\t{self.health}")
        print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}")
        time.sleep(1)
        delay_print(f"\n{self.name} used {self.move_name}!")
        time.sleep(1)
        print(f"\n{self.name}\t\tHealth:\t{self.health}")
        print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}")
        time.sleep(1)


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

    def use_move(self, pokemon2, move_index):
        self.move_name = self.moves[move_index]
        damage = random.randint(5, 20)
        pokemon2.health -= damage
        pokemon2_move_index = random.randint(0, len(pokemon2.moves)-1)
        pokemon2.move_name = pokemon2.moves[pokemon2_move_index]
        pokemon2_damage = random.randint(5, 20)
        self.health -= pokemon2_damage

        while (self.health > 0) and (pokemon2.health > 0):
            print(f"\n{self.name}\t\tHealth:\t{self.health}")
            print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}")
            
            time.sleep(2)
            print(f"\nGO {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("\nPick a move: "))
            self.use_move(pokemon2, index-1)
            
            time.sleep(2)
            delay_print(f"{self.name} used {self.move_name}!")
            time.sleep(1)
            delay_print(f"\n{self.move_name} caused {damage} damage.")
            time.sleep(1)
            print(f"\n{self.name}\t\tHealth:\t{self.health}")
            print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}") 
            time.sleep(2)

            if pokemon2.health <= 0:
                delay_print(f"\n{pokemon2.name} fainted. You win!")
                print("\n---WELL PLAYED! BYE BYE---")
                exit()
                
            
            print(f"\nGO {pokemon2.name}!")
            pokemon2.use_move(self, pokemon2_move_index)
            time.sleep(3)
            delay_print(f"{pokemon2.name} used {pokemon2.move_name}!")
            time.sleep(2)
            delay_print(f"{pokemon2.move_name} caused {pokemon2_damage} damage.")
            time.sleep(1)
            print(f"\n{self.name}\t\tHealth:\t{self.health}")
            print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}") 
            time.sleep(1)

            if self.health <= 0:
                delay_print(f"{self.name} fainted. You lose...")
                print("---WELL PLAYED! BYE BYE---")
                exit()

            # print(f"GO {pokemon2.name}!")
                                
            # for i, x in enumerate(pokemon2.moves):
            #     print(f"{i+1}.", x)
            # index = int(input("\nPick a move: "))
            # pokemon2.use_move(self, index-1)
            
            # time.sleep(2)
            # delay_print(self.s2_attack)

            # print(f"\n{self.name}\t\tHealth:\t{self.health}")
            # print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}") 
            # time.sleep(1)

            # if self.health <= 0:
            #     delay_print("\n...\t" + self.name + "\tFainted. \n\nYou lose...")
            #     exit()




if __name__ == '__main__':
    Charizard = Pokemon("Charizard", "Fire", ["Flamethrower", "Fly", "Blast", "Fire Punch"], {"ATTACK": 12, "DEFENSE": 8}, 100)
    Blastoise = Pokemon("Blastoise", "Water", ["Water Gun", "Fly", "Blast", "Fire Punch"], {"ATTACK": 12, "DEFENSE": 8}, 100)
    Venusaur = Pokemon("Venusaur", "Grass", ["Vine wip", "Fly", "Blast", "Fire Punch"], {"ATTACK": 12, "DEFENSE": 8}, 100)

Charizard.reset()
Blastoise.reset()
Venusaur.reset()

Charizard.fight(Venusaur)
Charizard.use_move(Venusaur, 0)
                  