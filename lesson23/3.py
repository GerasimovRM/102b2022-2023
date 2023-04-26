class Line:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        return self.k * x + self.b


line = Line(2, 1)  # 2x+1
print(line(5))

