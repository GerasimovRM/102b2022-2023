lst = []
while True:
    st = input()
    if st == 'разбитое корыто':
        break
    lst.append(st)

for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
        if len(lst[j]) > len(lst[j + 1]):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(*lst, sep='\n')