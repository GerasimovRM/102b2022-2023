
def func(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                return i, j
    return None, None


matrix = [[1, 2, 3], [4, 1, 6], [3, 1, 7]]
x, y = func(matrix)
print(x, y)