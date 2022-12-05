number = float(input())
count = 0
while number <= 36.6:
    if number < 0:
        count += 1
    number = float(input())
print(count)