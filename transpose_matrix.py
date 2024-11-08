#This is the code for practicing matrix implementation in python
matrix = []
nrow = int(input("Please enter the number of rows you want: "))
ncol = int(input("Please enter the number of col you want: "))

for _ in range(nrow):
    row = []
    for _ in range(ncol):
        ele = int(input("Please enter the element in the matrix: "))
        row.append(ele)

    matrix.append(row)

print()
print("The matrix that youy have enetered is : ")
for row in matrix:
    print(row)

# Transposing a matrix

trans_matrix = [[0 for _ in range(nrow)]for _ in range(ncol)]
print("The fresh matrix is : ")
for row in trans_matrix:
    print(row)

# now swap place the elements in position

for i in range(nrow):
    for j in range(ncol):
        if i != j:
            trans_matrix[i][j] = matrix[j][i]
        else:
            trans_matrix[i][j] = matrix[i][j]

print("The matrix after transpose is: ")
for row in trans_matrix:
    print(row)