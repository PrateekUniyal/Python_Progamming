# based on the number of legs, numbers of heads and horns return the total number of rabbits,chickens and cows

def get_animals_count(legs_number, heads_number, horns_number):
    cows = horns_number // 2 # getting number of cows
#     totalanimals = heads_number # total animals
    remaining_head = heads_number - cows # getting the number of rabbits and chicken
    remaininglegs = legs_number - cows * 4 # getting legs of rabbits and chickens
    rabbits = 0
#     while sum != totallegs:
#         sum = (rabbits * 4) + (chicken * 2)
#         rabbits += 1
#         chicken -= 1
    rabbits = (remaininglegs // 2) - remaining_head
    chicken = remaining_head -rabbits
    ans = {
        'rabbits' : rabbits ,
        'chickens': chicken ,
        'cows' : cows
    }
    return ans

legs_number = int(input("Please enter the number of legs: "))
heads_number = int(input("Please enter the number of heads: "))
horns_number = int(input("Please enter the number of horns: "))
print(get_animals_count(legs_number,heads_number,horns_number))
