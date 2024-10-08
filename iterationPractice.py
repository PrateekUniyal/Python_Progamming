# program to print natural numbers

num = int(input("Please enter the number to print the sequence-find the sum-print the table  "))
for i in range(1,num+1):
    print(i)

# program to print Sum of natural nuumbers

sum = 0
for i in range(1,num+1):
    sum = sum + i
print(sum)

# program to print multiplication table
i=1
mult = 1
for i in range(1,11):
    mult =num * i
    print(num,"X",i,"=",mult)

# program to print the even numbers

n = int(input("Please enter a  number to find even numbers and odd numbers "))
for i in range(0,n+1):
    if i % 2 == 0:
        print(i," is even")
    else:
        print(i," is odd")

