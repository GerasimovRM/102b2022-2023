lst = list(range(100))
it_filter = filter(lambda x: x % 2 == 0, lst)
print(next(it_filter))
print(next(it_filter))
print(*it_filter)

