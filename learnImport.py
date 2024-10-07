#import random
from random import randrange,random

# prob = random.random()    # first the module name.and the name of the function to use
prob = random()
print(prob)

dice_throw = randrange(1,7) #give me an integer from 1,2,3,4,5,6 but not 7
print(dice_throw)