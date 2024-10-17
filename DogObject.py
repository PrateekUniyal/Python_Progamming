# Program to understand class and object through example of Dog
class Dog: # A class by the name Dog is created
    def __init__(self, name, breed, age) : # Constructor which takes input self, name, breed , age
        self.name = name # give the name of current object the name passed
        self.breed = breed # give the current object breed the breed passed
        self.age = age # give the current object age the age passed

    def bark(self): # this is the capabilty  of the class Dog
        return(f"{self.name} is saying WOOF!")

dog1  = Dog("Buddy" , "Husky" , 3) # create an object for class Dog
dog2 = Dog("Andy" , "German Shepherd" , 5)
dog3 = Dog("Daisy" , "Pug" , 1)
print(dog1.bark()) # invoke the function bark()through a class object
print(dog2.bark())
print(dog3.bark())
