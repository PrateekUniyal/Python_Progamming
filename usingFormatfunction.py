# using .format method
details = [("ABC", 1), ("XYZ",2), ("KLM",3)]
for  person in details:
    name = person[0]
    rank = str(person[1])
    # print("Hello! "+name+" has got the ranking "+rank+".")
    print("Hello! {} has got the ranking {}".format(name,rank)) # using format method.

print("The above is the rank details.")
number = 81.23441313
print("The decimal number is : ",number)
print("The decimal number after using format method is: {:.4f}".format(number))

a = 2
b= 3

print(f"The value of a is {a} and the value of b is {b}.")
print(f"The sum of {a} + {b} is {a+b}")
