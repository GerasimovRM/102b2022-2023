def func1(x):
    return x ** 2


def func2(x):
    return x ** 3


def my_func(operator, x):
    return operator(x)


print(my_func(func1, 4))
