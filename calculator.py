# program to make a simple calculator
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
print("Enter 1 for sum, 2 for substraction, 3 for multiplication, 4 for division")
choice = int(input("Please enter your choice: "))
if choice == 1:
    total = a + b
    print("The sum is : ",total)
elif choice == 2:
    sub = a - b
    print("The substraction is : ", sub)
elif choice == 3:
    pro = a * b
    print("The product is : ", pro)
elif choice == 4:
    div = a // b
    print("The division is : ", div)
else:
    print("Invalid choice")

