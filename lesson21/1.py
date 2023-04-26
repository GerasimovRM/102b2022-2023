class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def info(self):
        print(f"{self.name} {self.weight}")

    def set_weight(self, new_weight):
        self.weight = new_weight


a = Fruit("apple", 300)
b = Fruit("orange", 200)
c = Fruit("bananananana", 150)
print(a.name, b.name, c.name)
print(a.weight, b.weight, c.weight)
a.info()  # Fruit.info(a)
a.weight = 40
a.info()
a.set_weight(70)
a.info()


