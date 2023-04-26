from functools import reduce
from itertools import chain
from random import random

count = 0


def func(x):
    global count
    count += 1
    return x + count


def func2(lst):
    lst.append(random())
    return lst.copy()


print(func(5))
print(func(5))
print(func(5))
print(func(5))

lst = [1, 2, 3]
print(func2(lst))
print(func2(lst))
print(func2(lst))
print(func2(lst))

a = '123'
b = None
c = 2345
print((a or b or c))
if any(map(lambda x: x is not None, [a, b, c])):
    print("YES")

a = [False, False, False]
print(all(a))
print(any(a))
k1 = [1, 2]
k2 = [2, 3]

k = ['345', '345547', '456234', 'dfugdsfis']
print("".join(k))
print(reduce(lambda a, b: a + b, k))
print("".join(chain(*k)))
