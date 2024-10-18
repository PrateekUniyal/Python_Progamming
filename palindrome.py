# program to check if input is palindrome or not.
n = input("Please enter the number to check for palindrome: ")
rev = n[::-1]
print(f"The reversed input  is : {rev}")
if rev == n:
    print("The input palindrome!")
else:
    print("Not a palindrome.")