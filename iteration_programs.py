# for loop in python
mylist = ["one", "two", "three", "four", "five"]
for color in ["red", "blue", "green", "yellow", "white", "black"]: # color is the loop variable
    print("The color present in the sequence is ",color)
for achar in "Hello world":
    print(achar)

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
for acolor in ["Yellow", "Red", "Green","Black"]:
    alex.color(acolor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
