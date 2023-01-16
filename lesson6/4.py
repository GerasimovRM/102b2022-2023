max_value = -float("inf")
curse = False
while True:
    number = int(input())
    if number > max_value:
        max_value = number
    elif max_value % 10 == number:
        curse = True
        break

    if number < 0:
        break
if curse:
    print("Проклятье!")
else:
    print(max_value)