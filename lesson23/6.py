class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        new_value = self.value + self.step
        if new_value > self.stop:
            raise StopIteration
        self.value = new_value
        return new_value

    def __iter__(self):
        while True:
            yield next(self)


a = FRange(1, 5)
for i in a:
    print(i)