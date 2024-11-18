# program to find the sum of n natural number(s) using recursion
def find_sum(number,total):
    if number == 0:
        return total
    else:
        total += number
        print(f" The sum uptill now is : {total}")
        return find_sum(number -1,total)
number = int(input("Please enter the number upto which we have to find sum: "))
if number >= 0:
    print(f"The sum upto {number} is {find_sum(number,0)}.")
else:
    print("Sorry you entered invalid input.")