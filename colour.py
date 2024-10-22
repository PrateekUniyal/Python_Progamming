# program to print the colours

class color:
    def __init__(self,name):
        self.name = name
        print("Constructor completed its task!")
        print()

    def display(self):
        print(f"The color which called this method is {self.name}.")


color1 = color("Black")
color2 = color("White")
color3 = color("Blue")
color4 = color("Red")
color5 = color("Green")

color1.display()
color2.display()
color3.display()
color4.display()
color5.display()