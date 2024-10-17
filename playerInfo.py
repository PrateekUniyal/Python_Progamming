# This code stores information for the players
import random
class Player:
    def __init__(self, name, score, power):
        self.name = name
        self.power = random.randint(1,10)
        self.score = 0

    def display_info(self):
        print(f"The current stats for {self.name} are:-")
        print(f"Power: {self.power}")
        print(f"Score:{self.score}")
        print("**************************************************>")
        return

def battle( p1power, p2power):
    p1power = player1.power
    p2power = player2.power
    if p1power > p2power:
            player1.score += 1
    elif p2power > p1power:
            player2.score += 1
    print("The battle is over. generating results...")
    print("*****************************************>")
def checkScore():
        if player1.score > player2.score:
            print(f"The Warrior is winning ! with a score of {player1.score}")
            print("*******************************************************>")
        elif player1.score < player2.score:
            print(f"The Viking is winning ! with a score of {player2.score}")
            print("*******************************************************>")
        else:
            print("It is a Tie!")




player1 = Player("Warrior",0,0)
player2 =Player("Viking", 0, 0)

player1.display_info()
player2.display_info()

# print(player1.power)
# print(player2.power)

battle(player1.power, player2.power)

checkScore()

player1.display_info()
player2.display_info()