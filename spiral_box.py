# program to create a spiral box
row = 8
col = 5

# array = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# for row in array:
#     print(row)
#
# for row in array:
#     for element in row:
#         print(element)
#     print()
arr = [[0 for ele in range(col)] for r in range(row)]
# arr = [[0 for r in range(row)] for ele in range(col)]
for row in arr:
    print(row)
print("********************************************************")

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i==0 or i==len(arr)-1:
            arr[i][j] = 1
        if j ==0 or j == len(arr)-1:
            arr[i][j] = 1
        if i == len(arr)-1 or i == 0:
            arr[i][j] = 1
        if j == len(arr)-1 or i == 0:
            arr[i][j] = 1

for row in arr:
    print(row)
print()
print("*********************************************************************")
print()
# array = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in array:
#     for item in row:
#         print(item, end=" ")
#     print()



