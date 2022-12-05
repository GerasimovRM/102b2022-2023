number = int(input())
ost = 0
while number != 0:
    ost = number % 12
    number //= 12
print(ost)

