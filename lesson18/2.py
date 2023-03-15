from itertools import chain


def is_add_elem(elem):
    global s
    if elem in s:
        return False
    s.add(elem)
    return True


s = set()

n = int(input())
lst = [input().replace(".", "").split() for _ in range(n)]
print(lst)
lst = list(enumerate(chain(*lst)))
print(lst)
lst = list(filter(lambda x: x[1][0].isupper(), lst))
lst = list(filter(lambda x: is_add_elem(x[1]), lst))
print(lst)
lst = sorted(lst, key=lambda x: x[1])
print(*map(lambda x: f'{x[0]} - {x[1]}', lst), sep='\n')

