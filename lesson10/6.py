lst = []
for i in range(int(input())):
    x, y = int(input()), float(input())
    lst.append((x, y))

for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
        if lst[j] < lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

# for elem in lst:
#     print(elem)
print(*lst, sep='\n')