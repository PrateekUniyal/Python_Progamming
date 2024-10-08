# python program to find the factorial of a number

n = int(input("Please enter the number to find the factorial "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("The factorial is ",fact)
