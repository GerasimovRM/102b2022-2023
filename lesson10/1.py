a = 1, 2, 3
print(a, a[0], a[:2], type(a))

a = 3
b = 4
a, b = b, a
# print('1' > 2) Error
a1 = (1, 'abc')
a2 = (1, 'abv')
lst1 = list(a1)
a = tuple(lst1)
lst = [1, 2, 3]
st = str(lst)
for sym in st:
    print(sym)

lst = [1, 4]
lst2 = [1, 4, print]
print(lst2 > lst)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1 > s2, s2 > s1)
