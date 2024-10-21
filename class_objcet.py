# program to understand structure of a class and its objects
class this_is_a_class:
    def __init__(self,name):
            self.name = name
            print(f"We are inside the constructor method\t ---> The {self.name} is created.")

    def display(self,name):
        print(f"We are inside the function display with\t ---> {self.name}")

object1 = this_is_a_class("object1")
object2 = this_is_a_class("object2")

object1.display(object1)
object2.display(object2)