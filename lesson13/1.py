lst = (1, 2, 3)
d = {1: "sdoufhsdou", 2: None, "key": 'ключ'}
print(d, d[1], d["key"])
lst = {elem ** 2 for elem in range(1, 11)}
d[5] = 4536456
print(d)
elem = d.pop(6, None)
print(d, elem)

di = {}
for i in range(1, 11):
    di[i] = i ** 2
print(di)

di2 = {i: i ** 2 for i in range(1, 11)}

print(len(di2))
print(5 in di2, 11 in di2)
for key in di2:
    print(key, di2[key])

lst = list(di2)
print(lst)
lst2 = [di2[key] for key in di2]
print(lst2)
keys = list(di2.keys())
values = list(di2.values())
items = list(di2.items())
print(keys, type(keys))
print(items)
di3 = dict(items)
print(di3)
lst2 = [(1, 546), (24, 356), (45, 56756)]
for x, y in lst2:
    print(x, y)

for key, value in di2.items():
    print(key, value)

t = di2[3]
t2 = di2.get(20)
print(t, t2)
di4 = {1: 345, 2: 345664}
di5 = {2: 654}
print(di4)
di4.update(di5)
print(di4)
