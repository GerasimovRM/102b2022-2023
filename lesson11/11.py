n = int(input())
lst = [elem ** 2 for elem in range(1, n) if set(str(elem)) == {"1"} ]
print(*lst, sep=', ')

