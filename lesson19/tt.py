def generator_decorator(n):
    def decorator(func):
        def new_func(*args, **kwargs):
            print("*" * n)
            result = func(*args, **kwargs)
            print("*" * n)
            return result
        return new_func
    return decorator


@generator_decorator(3)
def f(a, b):
    print(a + b)


def f2(a):
    return a * 2


if __name__ == "__main__":
    f(1, 2)
    print(generator_decorator(5)(f2)(4))
