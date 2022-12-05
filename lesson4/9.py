max_value = int(input())
number = int(input())
if number > max_value:
    max2_value = max_value
    max_value = number
else:
    max2_value = number

while abs(number) < 1000:
    if number > max_value:
        max2_value = max_value
        max_value = number
    elif number > max2_value:
        max2_value = number
    number = int(input())
print(max2_value)