# program to understand classes

class partyanimal : # creating a class
    def __init__(self): # constructor method
        self.x = 0

    def party(self): # another method
        self.x = self.x + 1
        print("So far",self.x)

an = partyanimal() # creating an instance/object of class partyanimal

an.party()
an.party()
an.party()