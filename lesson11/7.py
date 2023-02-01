lst = [i for i in range(1, 100) if sum([int(sym) for sym in str(i)]) == 7]
print(lst)

k = [1, 2, 3]
k = k * 4
print(k)
lst = [[1, 2, 3]] * 3
lst[0][0] = 4
print(lst)
lst = [[1, 2, 3] for _ in range(10)]
lst[0][0] = 4
print(lst)

lst = [1, 2, 3]
lst2 = lst[:]
lst2[0] = 4
print(lst)
