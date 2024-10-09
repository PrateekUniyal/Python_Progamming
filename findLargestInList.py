'''Program to find the largest number in the list'''
my_list = []
print("Please enter the numbers in the list: ")
for i in range(1,6):
    n = int(input())
    my_list.append(n)

largest =my_list[0]
for i in my_list[1:]:
    if largest < i:
        largest = i

print("The largest number in the list is : ",largest)