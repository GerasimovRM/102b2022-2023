d = {}
for _ in range(int(input())):
    number, name = input().split()
    if name not in d:
        d[name] = []
    d[name].append(number)
for _ in range(int(input())):
    name = input()
    if name in d:
        print(*d[name])
    else:
        print('Нет в телефонной книге')
