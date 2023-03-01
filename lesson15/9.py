def func(z, x=1, y=2, *args, kw=3, kj=4, **kwargs):
    print(z, x, y, args, kw, kj, kwargs)
    return x ** 2 + y ** 2 + z ** 2


print(func(1), func(2), func(3, 4, 2, 456, 56, 57, 3456, 456, 4, 67, kj=10))
func(1, 2, 3, 1, 2, kw=10, t=3)

def func(*args, **kwargs):
    pass
