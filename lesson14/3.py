def func(x):
    global y, z
    y += 1
    return x ** 2 + y + z


y = 4
z = 1
print(func(4), y)
print(func(4), y)
print(func(4), y)
print(func(4), y)
print(type(func))
my_different_name = func
print(my_different_name(4), y)
print(id(my_different_name), id(func))


