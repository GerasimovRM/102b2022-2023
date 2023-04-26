class Selector:
    def __init__(self, values):
        self.__odds = list(filter(lambda x: x % 2 == 1, values))
        self.__evens = list(filter(lambda x: x % 2 == 0, values))

    def get_evens(self):
        return self.__evens

    def get_odds(self):
        return self.__odds

    def __func(self):
        pass

    def _func(self):
        pass


a = Selector([1, 2, 3, 4, 5])
a.__odds = [15, 20]
print(a.get_odds())
