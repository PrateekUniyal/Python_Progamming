# Python program to find factorial of a number using recursion
def find_fact(number,result):
    if number == 0 or number == 1:
        return result
    else:
        result = number * result
        print(f"The result till now is : {result}")
        return find_fact(number - 1,result)

number = int(input("Please enter the number to find factorial: "))
print(f"The factorial of {number} is {find_fact(number,1)}.")
