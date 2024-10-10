# a sequence is an ordered collection
s = "Hello World"
print(len(s))
s = """This is a multi line string"""
print(s)

# A string is a sequence of characters

# list is a sequence of any type of value

myList = ["one" , 2, 'three']
print(myList)

# tuples are immutable that means once created it cant be changed
myTuple = ("one", 2 ,'three')
my_tuple = (100)
print(type(myList))
print(type(myTuple))
print(type(my_tuple))
my_tuple = (100,)
print(type(my_tuple))

#index operator

str = "Hello"
print(str)
print(str[0])
print(str[4])
print(myList[2])
print(str[len(str)-1])

fruit ="Grape"
print(fruit[len(fruit)//2])