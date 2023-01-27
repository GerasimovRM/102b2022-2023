lst = []
while True:
    number = int(input())
    if not number:
        break
    lst.append(number)

for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

# for i in range(len(lst)):
#     if i == len(lst) - 1:
#         print(lst[i])
#     else:
#         print(lst[i], end='->')
print(*lst, sep='->')

