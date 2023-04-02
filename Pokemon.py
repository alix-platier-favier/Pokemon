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
                    delay_print("It's not very effective...\n")
                    delay_print("It's not very effective...\n")

                elif pokemon2.types == version[(i+1)%4]:
                    pokemon2.attack *= 2
                    pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /=2
                    delay_print("It's not very effective...\n")
                    delay_print("It's super effective!\n")

                elif pokemon2.types == version[(i+2)%4]:
                    self.attack *= 2
                    self.defense *= 2
                    pokemon2.attack /= 2
                    pokemon2.defense /=2
                    delay_print("It's super effective!\n")
                    delay_print("It's not very effective...\n")

        print(f"\n{self.name}\t\tHealth:\t{self.health}")
        print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}")
        time.sleep(1)
        delay_print(f"\n{self.name} used {self.move_name}!")
        time.sleep(1)
        print(f"\n{self.name}\t\tHealth:\t{self.health}")
        print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}")
        time.sleep(1)



    def fight(self, pokemon2):

        self.reset()
        pokemon2.reset()

        print("------POKEMON FIGHTING------")
        print(f"\n{self.name}")
        print("TYPE:", self.types)
        print("ATTACK:", self.attack)
        print("DEFENSE:", self.defense)
        print("LVL:", 10)
        print("\nVS")
        print(f"\n{pokemon2.name}")
        print("TYPE:", pokemon2.types)
        print("ATTACK:", pokemon2.attack)
        print("DEFENSE:", pokemon2.defense)
        print("LVL:", 10)

        while (self.health > 0) and (pokemon2.health > 0):
            self.player_turn(pokemon2)
            self.opponent_turn(pokemon2)

        time.sleep(2)

    def use_move(self, pokemon2, move_index):
        self.move_name = self.moves[move_index]
        damage = random.randint(5, 20)
        pokemon2.health -= damage
        pokemon2_move_index = random.randint(0, len(pokemon2.moves)-1)
        pokemon2.move_name = pokemon2.moves[pokemon2_move_index]
        pokemon2_damage = random.randint(5, 20)
        self.health -= pokemon2_damage
        return damage, pokemon2_move_index, pokemon2_damage


    def print_pokemon_stats(self, pokemon2):
        print(f"\n{self.name}\t\tHealth:\t{self.health}")
        print(f"{pokemon2.name}\t\tHealth:\t{pokemon2.health}")

    def print_moves(self):
        for i, x in enumerate(self.moves):
            print(f"{i+1}.", x)

    def player_turn(self, pokemon2):
        print(f"\nGO {self.name}!")
        self.print_moves()
        index = int(input("\nPick a move: "))
        damage, pokemon2_move_index, pokemon2_damage = self.use_move(pokemon2, index-1)
        self.damage = damage
        self.pokemon2_move_index = pokemon2_move_index
        self.pokemon2_damage = pokemon2_damage
        time.sleep(1)
        delay_print(f"{self.name} used {self.move_name}!")
        time.sleep(0.5)
        delay_print(f"\n{self.move_name} caused {self.damage} damage.")
        time.sleep(0.5)
        self.print_pokemon_stats(pokemon2)

        if pokemon2.health <= 0:
            delay_print(f"\n{pokemon2.name} fainted. You win!")
            print("\n---WELL PLAYED! BYE BYE---")
            exit()

    def opponent_turn(self, pokemon2):
        print(f"\nGO {pokemon2.name}!")
        move_index = random.randint(0, len(pokemon2.moves)-1)
        move = pokemon2.moves[move_index]
        damage = pokemon2.use_move(self, move_index)[2]
        self.health -= damage
        time.sleep(1)
        delay_print(f"{pokemon2.name} used {move}!")
        time.sleep(0.5)
        delay_print(f"\n{move} caused {damage} damage.")

        if self.health <= 0:
            delay_print(f"\n{self.name} fainted. {pokemon2.name} wins!")
            print("\n---GAME OVER---")
            exit()


def delay_print(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.05)

if __name__ == "__main__":
    Charmander = Pokemon("Charmander", "Fire", ["Ember", "Scratch", "Tackle", "Fire Punch"], {"ATTACK": 12, "DEFENSE": 8}, 100)
    Squirtle = Pokemon("Squirtle", "Water", ["Bubblebeam", "Tackle", "Headbutt", "Surf"], {"ATTACK": 10, "DEFENSE": 10}, 100)
    Bulbazaur = Pokemon("Bulbazaur", "Earth", ["Vine wip", "Razor Leaf", "Tackle", "Leech Seed"], {"ATTACK": 8, "DEFENSE": 12}, 100)

    print(f"\nGet ready for a battle between {Squirtle.name} and {Bulbazaur.name}!")
    time.sleep(1)
    print("\nLETS GO!")
    time.sleep(1)

    Squirtle.fight(Bulbazaur)