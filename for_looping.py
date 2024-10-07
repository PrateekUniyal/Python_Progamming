#For loop in python

print("This will be executed first")

for _ in range(3):
    print("This will be printed 3 times")
    print("This will also be executed 3 times")

print("We are now outside the loop")

import turtle
wn = turtle.Screen()
elan = turtle.Turtle()
distance = 50
for _ in range(30):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10

