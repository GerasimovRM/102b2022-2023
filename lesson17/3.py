def generate_power(pow):
    def func(x):
        return x ** pow

    return func


my_square = generate_power(2)
print(my_square(3))
