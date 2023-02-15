d = {}
for _ in range(int(input())):
    key, value = input().split(maxsplit=1)
    d[key] = value
for _ in range(int(input())):
    key = input()
    if key in d:
        print(d[key])
    else:
        print('Нет в словаре')

# d = {key: value for key, value in [input().split(maxsplit=1)
#      for _ in range(int(input()))]}
# for _ in range(int(input())):
#     print(d.get(input(), "Нет в словаре"))