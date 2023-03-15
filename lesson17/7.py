print(*filter(lambda t: sum(map(int, str(t))) == 4,
                 map(lambda x: x ** 2, range(10, 1000))))
print(*filter(lambda x: sum(map(int, str(x ** 2))) == 4, range(10, 1000)))


def func(xx, yy):
    return xx + yy


x, y, z = map(int, input().split())
x, y, z = map(lambda xx: func(xx, 3), (x, y, z))
print(x, y, z)

it = iter(range(10))
for elem in it:
    print(elem)
for elem in it:
    print(elem)



