# Program to build a simple turn based battle game.
class Battle:
    def selectionMenu(self):
        print("1 ----> warrior || 2 -----> mage|| 3 ----> assassin")
        select = input("Player 1 select your fighter: ")
        if select == '1':
            choice1 = 'w'
            wname = input("Please enter the name of your warrior: ")
            warrior = Warrior(wname)
            warrior.details()
        elif select =='2':
            choice1 ='m'
            mname = input("Please enter the name of your mage: ")
            mage = Mage(mname)
            mage.details()
        elif select =='3':
            choice1 ='a'
            aname = input("Please enter the name of your assassin: ")
            assassin = Assassin(aname)
            assassin.details()
        else:
            print("Invalid input.")

        print("1 ----> warrior || 2 -----> mage|| 3 ----> assassin")
        select = input("Player 2 select your fighter: ")
        if select == '1':
            choice2 = 'w'
            wname = input("Please enter the name of your warrior: ")
            warrior = Warrior(wname)
            warrior.details()
        elif select == '2':
            choice2 ='m'
            mname = input("Please enter the name of your mage: ")
            mage = Mage(mname)
            mage.details()
        elif select == '3':
            choice2='a'
            aname = input("Please enter the name of your assassin: ")
            assassin = Assassin(aname)
            assassin.details()
        else:
            print("Invalid input.")

        

    def battleground(self,ch1,ch2):
        pass

class Warrior:
    def __init__(self,name):
        self.name = name
        self.hp = 260
        self.power = 40


    def details(self):
        print(f"The details of your {self.name} are: ")
        print(f"Health is {self.hp}")
        print(f"Power is {self.power}")
        print("||||||||||||||||||||||||||||||||||||||||")

  # ---> Abilities
  #     Iron Skin: Reduce damage of the next attack received in 50% and regenerate your health by 40 points. (buff)
  #     Blade Storm: Attacks with a power of 75 points.(special attack)

class Mage:
    def __init__(self,name):
        self.name = name
        self.hp = 200
        self.power = 50

    def details(self):
        print(f"The details of your {self.name} are: ")
        print(f"Health is {self.hp}")
        print(f"Power is {self.power}")
        print("******************************************")


 # ---> Abilities
 #      Arcane Shield: Absorb the next damage received. (buff)
 #      Fireball: Attacks with a power of 90 points.(special attack)

class Assassin:
    def __init__(self,name):
        self.name = name
        self.hp = 235
        self.power = 30

    def details(self):
        print(f"The details of {self.name} are: ")
        print(f"Health is {self.hp}")
        print(f"Power is {self.power}")
        print("||||||||||||||||||||||||||||||||||||||||")
    # ---> Abilities
    #     Assassin's instinct: Increases your power by 40 points for three attacks. (buff)
    #     Lacerate: Inflicts the equivalent of 2x your power points. (special attack)


battle = Battle()
battle.selectionMenu()