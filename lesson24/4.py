class MyList(list):
    def sum(self):
        return sum(self)


lst = MyList({1, 2, 3, 4, 5})
print(lst[:3], lst.sum())
