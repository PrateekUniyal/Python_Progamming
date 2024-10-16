# we have a number , we want to know the highest power closest to the number

n = int(input("Please enter the number: "))
pow_ = int(input("Please enter the power: "))
cube = 0
for i in range(1,n):
    cube = i ** pow_
    if cube > n:
        answer = cube
        break

print("The answer is : ",answer)
