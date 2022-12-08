money = 1
price = int(input())
count = 0
while money < price:
    money *= 10
    count += 1
print(count)
