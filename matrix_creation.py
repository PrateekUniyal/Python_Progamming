row = int(input("Please enter the number of rows: "))
col = int(input("Please enter the number of columns: "))

matrix = []
matrix = [[0 for _ in range(col)]  for _ in range(row)]

print()
print("The matrix created is :-")
for r in (matrix):
    print(r)

for i in range(row):
    for j in range(col):
        inp= int(input(f"Please enter the element at position [{i}] [{j}]: "))
        matrix[i][j] = inp

for row in matrix:
    print(row)