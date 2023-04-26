class A(object):
    def func_a(self):
        return 1


class B(A):
    def func_b(self):
        return 2


a = A()
a.func_a()
b = B()
print(a)