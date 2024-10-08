# Program to count the vowels in a string

s = input("Please enter the string to count vowels: ")
count =0
for char in (s):
    if char in 'aeiouAEIOU':
        count += 1
print("The number of vowels in the string are : ",count)