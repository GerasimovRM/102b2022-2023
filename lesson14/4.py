def func():
    global x
    x += 1


x = 4
for i in range(10):
    a = func()
    print(a, x)
