import random
from character import Character

class Game:

    def __init__(self, player1: Character, player2: Character):
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        #pass #TODO: Implement dice roll 1-6 and apply scaled attack power to defender
        defender.health = defender.health - attacker.attack_power

        return defender.health



    def start_battle(self):
        #pass #implement the battle loop where players take turns attacing
        rolled_dice_player_1 = random.randint(1,6)
        rolled_dice_player_2 = random.randint(1,6)


        
