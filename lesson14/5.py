matrix = [[1, 2, 3], [4, 1, 6], [3, 1, 7]]
zero_is_find = False
x, y = None, None
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            x, y = i, j
            zero_is_find = True
            break
    if zero_is_find:
        break
print(x, y)