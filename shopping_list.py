# program to build a simple shopping list.
print()
print("The items available for shopping are : ")
print("****************************************")
print("Apple : ₹20")
print("mango : ₹40")
print("Spinach : ₹30")
print("Carrot : ₹20")
print("Milk : ₹60")
print("Butter: ₹30")
print("*****************************************")

class shopping_list:
    def __init__(self, name, budget):
         self.name = name
         self.budget = budget

    def check_balance(self):
        print(f"{self.name} has ₹{self.budget}.")

    def shopping(self):
        choice = '0'
        total = 0
        lst = []
        print("Add a for apple followed by quantity.")
        print("Add m for mango followed by quantity.")
        print("Add s for spinach followed by quantity.")
        print("Add c for carrot followed by quantity.")
        print("Add mi for milk followed by quantity.")
        print("Add b for butter followed by quantity.")
        print("************************************************")
        choice = input("Please enter q to exit else press enter: ")
        while choice != 'q':
            item = input("Please enter the item to shop!: ")
            quantity = int(input("Please enter the quantity: "))
            if item == 'a':
                lst.append(f"{quantity} Apple")
                total = total +20*quantity
            elif item == 'm':
                lst.append(f"{quantity} Mango")
                total = total+40*quantity
            elif item == 's':
                lst.append(f"{quantity} Spinach")
                total = total + 30 * quantity
            elif item == 'c':
                lst.append(f"{quantity} Carrot")
                total = total + 20 * quantity
            elif item == 'mi':
                lst.append(f"{quantity} Milk")
                total = total+60*quantity
            elif item == 'b':
                lst.append(f"{quantity} Butter")
                total = total + 30 * quantity
            choice = input("You can enter q to complete shopping or press enter to add more:")
        print()
        print("********************************************")
        print("THE BILL GENERATED IS:")
        print("The items in your shopping list are: ")
        for it in lst:
            print(it+"\t")
        print(f"Your grand total is : {total}")
        print()
        print("***********THANK YOU FOR SHOPPING*************")
        return total
    def compare(self,budget,total):
        if budget >= total:
            print("Great your budget is more than expense,Happy Shopping!.")
        else:
            print("Sorry your budget is less than your expense.")

budget1 = 550
budget2 = 1000
budget3 = 150
budget4 = 200

person1 = shopping_list("John",550)
person2 = shopping_list("Sara", 1000)
person3 = shopping_list("Mark", 150)
person4 = shopping_list("Julian", 200)


person1.check_balance()
person2.check_balance()
person3.check_balance()
person4.check_balance()

print("***********************************")
print()
total1 = person1.shopping()
total2 = person2.shopping()
total3 = person3.shopping()
total4 = person4.shopping()

person1.compare(budget1,total1)
person2.compare(budget2,total2)
person3.compare(budget3,total3)
person4.compare(budget4,total4)
