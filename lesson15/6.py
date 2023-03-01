st = [1, 2, 3]
print(id(st), st)
st += [1, 2, 3]
print(id(st), st)
st = st + [1, 2, 3]
print(id(st), st)


st = '123'
print(id(st))
st = st + '123'
print(id(st))