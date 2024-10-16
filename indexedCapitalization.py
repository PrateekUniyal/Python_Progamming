# program to capitalize the character at a given index
s = input("Please enter the string : ")
ind = []
ind =(input("Please enter the list of indexes: "))
print(type(ind))
print(ind)
ind_ = [int(i) for i in ind.split()]
print(type(ind_))
print(ind_)
answer = ""
index = 0
for i in s:
        if index in ind_:
            answer = answer+i.upper()
            index += 1
        else:
            answer = answer+i
            index += 1
print(answer)

