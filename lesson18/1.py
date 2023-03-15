from itertools import count, cycle, repeat, chain, combinations, combinations_with_replacement, dropwhile, groupby, \
    permutations, zip_longest

it = count(100, 100)
lst = [next(it) for _ in range(10)]
print(lst)
lst = [next(it) for _ in range(10)]
print(lst)
lst = repeat(3, 100)
print(*lst)
# lst = list(range(10))
# it = cycle(lst)
# for elem in it:
#     print(elem)
s = {1: 345, 2: 56, 3: 567}
lst = [10, 15, 40]
st = '456'
print(*chain(s, lst, st))
print(*map(lambda x: "".join(x), combinations('ABCD', 3)))
print(*map(lambda x: "".join(x), combinations_with_replacement('ABCD', 3)))
print(*dropwhile(lambda x: x < 5, [1,4,6,4,1]))
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),("vehicle", "speed boat"), ("vehicle", "school bus")]
for group, values in groupby(things, lambda x: x[0]):
    print(group, *map(lambda value: next(reversed(value)), values))

lst = list(range(6))
print(*permutations(lst, 3))

print(*map(lambda x: pow(*x), [(2,5), (3,2), (10,3)]))

t = [1, 2, 3, 4, 5]
t2 = [564 ,657, 567]
t3 = [456, 456 ,866, 987]
print(*zip(t, t2, t3))
print(*zip_longest(t, t2, t3, fillvalue=list.pop))

lst = [lambda x: x ** 1, lambda x: x ** 2, lambda x: x ** 3]
print(lst)
for func in lst:
    print(func(2))



