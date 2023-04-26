k = 0


def func():
    global k
    k += 1
    return k if k < 3 else None

print(func())
print(func())
print(func())