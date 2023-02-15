d = {"янв": [],
     "фев": [],
     "мар": [],
     "апр": [],
     "май": [],
     "июн": [],
     "июл": [],
     "авг": [],
     "сен": [],
     "окт": [],
     "ноя": [],
     "дек": []}
for _ in range(int(input())):
    data = input().split()
    name, month = data[0], data[-1]
    d[month].append(name)
for key in d:
    d[key].sort()
for _ in range(int(input())):
    month = input()
    print(*d[month])

