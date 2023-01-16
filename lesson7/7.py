for x in range(2, int(input()) + 1):
    count = 0
    for i in range(2, x):
        if x % i == 0:
            count += 1
            break
    if count == 0:
        print(x)
