A = [[3, 2, -5],
     [2, -1, 3],
     [1, 2, -1]]
f = [-1, 13, 9]

M = list(map(list, zip(*(list(zip(*A)) + [f]))))
print(M)
for i in range(len(M) - 1):
    for j in range(i + 1, len(M)):
        temp = M[j][i] / M[i][i]
        for k in range(i, len(M) + 1):
            M[j][k] -= M[i][k] * temp
print(*M, sep='\n')
solution = [None] * len(M)
for i in reversed(range(len(M))):
    solution[i] = M[i][-1]
    for j in reversed(range(i + 1, len(M))):
        solution[i] -= M[i][j] * solution[j]
    solution[i] /= M[i][i]
print(solution)