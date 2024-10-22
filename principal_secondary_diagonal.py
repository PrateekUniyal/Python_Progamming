# program to find the principal and secondary diagonal
row = 3
col = 3
principal_diagonal= []
secondary_diagonal = []

matrix = [[1,2,3], [4,5,6],[7,8,9]]

i = 0
for lst in matrix:
    principal_diagonal.append((lst)[i])
    i += 1;
    if i == len(matrix):
        break

    j = len(lst) - 1

for lst in matrix:
    secondary_diagonal.append(lst[j])
    j -= 1
    if j < 0:
        break

print(f"The principal diagonal is : {principal_diagonal}")
print(f"The secondary diagonal is: {secondary_diagonal}")