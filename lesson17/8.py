lst = list(range(10, 20))
for i, elem in enumerate(lst):
    print(i, elem)


lst2 = 'abcdefgh'
lst3 = [23, 56, 67, 56, 34, 56]

print(*zip(lst2, lst3, range(10)))