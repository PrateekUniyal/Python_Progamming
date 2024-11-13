def command_analyzer(command,position):
    print(f'The current position is: {position}')
    dist = ''
    x = position[0]
    y = position[1]

    for i in command:
        if i.isalpha():
            al = i
        else:
            dist += i

    dist_i = int(dist)

    if al == 'A':
        x -= dist_i
    elif al == 'D':
        x += dist_i
    elif al == 'W':
        y += dist_i
    elif al == 'S':
        y -= dist_i

    position = [x,y]
    return(position)


def coordinate_helper(cmd):
    x = 0
    y = 0
    position =[x,y]
    for command in cmd:
        position = command_analyzer(command,position)
        print(f"The current position is :{position}")

    return tuple(position)

print("The input is :","A10","S10","D20","W20")
print(f'The final coordinate is : {coordinate_helper(["A10","S10","D20","W20"])}') # 10,10
# print(f'The final coordinate is : {coordinate_helper(["A10","S10","D20","W20"])}')