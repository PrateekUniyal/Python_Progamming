def get_matrix(n):
    if n == 1:
        return [[1]]

    mat = [[0 for _ in range(n)] for _ in range(n)]

    for lst in range(len(mat)):
        for ele in range(len(mat[0])):
            # if mat.index(lst) == lst.index(ele):
            #     ele = 1
            if ele == lst:
                mat[lst][ele] = 1

    return mat

print(get_matrix(5))