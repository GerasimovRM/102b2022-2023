def func():
    yield 1
    yield 2
    yield 3


def func2():
    return 1
    return 2
    return 3


class A:
    def __iter__(self):
        a, b = 1, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b


a = A()
f = iter(a)
print(next(f), next(f), next(f), next(f), next(f), next(f))
