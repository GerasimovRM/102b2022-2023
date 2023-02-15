numbers = [int(elem) for elem in input().split()]
result = []
for number in numbers:
    digits = 0
    zeros = 0
    units = 0
    while number != 0:
        if number % 2 == 0:
            zeros += 1
        else:
            units += 1
        digits += 1
        number //= 2
    result.append({"digits": digits, "units": units, "zeros": zeros,})
print(result)
