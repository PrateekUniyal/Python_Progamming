# Program to understand mutabilty of the list
fruits = ["Apple","Orange","Banana"]
print(fruits)

for fruit  in fruits:
    print(fruit,end="\t") # Printing beside each other in a single line

print(end="\n")

fruits[0] = "Mango"
fruits[-1] = "Kiwi"
for fruit in fruits:
    print(fruit,end="\t")

fruits.extend(["Papaya", "Berries"])
print(end="\n")
for fruit in fruits:
    print(fruit,end="\t")

fruits[1:4] = ["Grapes", "Avacado", "Watermelon"]
print(end="\n")
for fruit in fruits:
    print(fruit,end="\t")

print(end="\n")

letters = ['a','b','c','d','e']

print(letters)
letters[-4:-2] =[]
print(letters)
letters[1:3] = []
print(letters)

tuple_list = (1,2,3,4)
print(tuple_list)

#tuples and strings are immutable
