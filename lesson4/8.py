number = int(input())
max_value = number
min_value = number
while number != 0:
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number
    number = int(input())
print(min_value)
print(max_value)