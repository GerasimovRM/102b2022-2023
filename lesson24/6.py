from itertools import chain


class Matrix:
    def __init__(self, components):
        self.components = components

    def transpose(self):
        return Matrix(list(zip(*self.components)))

    def __iter__(self):
        return chain(*self.components)


m = Matrix([[3, 5], [7, 9]])
m2 = m.transpose()
for i in m:
    print(i)
