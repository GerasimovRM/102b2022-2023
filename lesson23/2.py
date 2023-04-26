from datetime import datetime


class Check:
    def __init__(self):
        self.lst = []
        self.time = datetime.now()

    def add_position(self, name, price):
        self.lst.append((name, price))

    def __iter__(self):
        return iter(self.lst)

    def __getitem__(self, item):
        return self.lst[item]


sjdgfksdgfskufewjs = Check()
sjdgfksdgfskufewjs.add_position('Молоко', 50)
sjdgfksdgfskufewjs.add_position('Курица', 250)
sjdgfksdgfskufewjs.add_position('Рыбу', 900)

for name, price in sjdgfksdgfskufewjs:
    print(name, price)

print(sorted(sjdgfksdgfskufewjs, key=lambda x: (x[1], x[0])))
print(sjdgfksdgfskufewjs[0], sjdgfksdgfskufewjs[1], sjdgfksdgfskufewjs[2])
print(*sjdgfksdgfskufewjs)

