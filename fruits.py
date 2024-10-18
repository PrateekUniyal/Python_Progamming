# Understanding objects and classes
class Fruit: # created a class
    def __init__(self,name,color): # defined a constructor
        self.name = name
        self.color = color

    def display_information(self): # defined a method to display information
        print(f"The name of the fruit is {self.name}. The color of {self.name} is {self.color}.")


class Person: # created another classs
    def __init__(self,name,profession): # created a constructor for this new class
        self.name = name
        self.profession = profession


    def person_details(self): # method to display content
        print(f"Hello my name is {self.name}. I am {self.profession}.")


    def favourite(self): # method to display favourite fruit
        if self.name == "John":
            print(f"{self.name} loves to eat Mango.")
        elif self.name == "Cody":
            print(f"{self.name} loves to eat Apple.")
        else:
            print(f"{self.name} loves to eat Kiwi.")


mango = Fruit("Mango", "Yellow") # made 3 objects/instances of class fruit
apple = Fruit("Apple", "Red")
kiwi = Fruit("Kiwi" , "Brown")

person1 = Person("John" , "Student") # made 3 objects/instances of class person
person2 = Person("Cody", "Athlete")
person3 = Person("Bob", "IT Developer" )


mango.display_information()
kiwi.display_information()
apple.display_information()

print("***************************************************************")

person1.person_details()
person2.person_details()
person3.person_details()

print("***************************************************************")

person1.favourite()
person2.favourite()
person3.favourite()
