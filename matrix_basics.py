# program to learn matrix operations

row =2
col =2

mat = [[0 for _ in range(row)] for _ in range(col)]
for row in mat:
    print(row)
mat[0][0] = 1
mat[col-1][col-1] = 1
print("*********************")
for row in mat:
    print(row)
