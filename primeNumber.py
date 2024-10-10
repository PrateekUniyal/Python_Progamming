# Program to find if the number is prime or not
n = int(input("Please enter the number to check for prime: "))
flag = 0
for i in range(1,n+1):
    # print(i)
    if n % i == 0:
        flag += 1

if flag == 2:
    print(n, "is Prime")
else:
    print(n, "is not Prime")