# program to find the power of a number
def find_power(number,power, result):
   if power == 0:
       return result * 1
   else:
       result = result * number
       print(f"The result up till now is {result}")
       return (find_power(number,power-1,result))


number = int(input("Please enter the number to find the power : "))
power = int(input("Please enter the number to raise the power to : "))

print(f"The {number} raised to the power {power} is {find_power(number,power,1)}")