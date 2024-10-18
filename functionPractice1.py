# Program to practice functions
def sum_ (a,b):
     sum = a + b
     return sum
def sub_ (a,b):
     if a > b:
         sub = a-b
         return sub
     elif a < b:
         sub = b-a
         return sub
     else:
         return 0
def mult_(a,b):
        pro = a*b
        return pro
def div(a,b):
      div = a // b
      return div

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The sum is : ", sum_(a,b))
print("The subtraction is : ", sub_(a,b))
print("The multiplication is : ", mult_(a,b))
print("The division is : ", div(a,b))
