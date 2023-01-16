while True:
    number = int(input())
    if number < 10:
        continue
    elif number > 100:
        break
    sqrt = int(number ** 0.5)
    print(sqrt)
print("ФИНАЛ")
