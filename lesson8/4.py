def func1(x):
    return x ** 2

def func2(x):
    return x ** 3


s = {func1, func2}
for func in s:
    print(func(4))
    