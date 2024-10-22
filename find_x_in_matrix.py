# program to find x in a 3x3 matrix
row=3 # define the number of  row
col=3 # define the number of column
mat = [[0 for _ in range(row)]for _ in range(col)] # create a 2d matrix with all element 0
for row in mat: # print the created matrix
    print(row)
mat[0][0] = 'x' # make element at 00 x
mat[1][2] = 'x' # make element at 12 x
print()
print("****************************************")
print()
for row in mat: # print the matrix after replacing 0 with x
    print(row)
    print()
print("*******************************************")
print()
for lst in mat: # this is for traversing between the rows
    for element in lst: # this is for traversing inside each row
        if element == "x":
            print(f"x is found at the index [{mat.index(lst)} {lst.index(element)}].") # first part is tye row index the second part is tye col index
        else:
            print(f"This element is 0 not x at index [{mat.index(lst)} {lst.index(element)}].")