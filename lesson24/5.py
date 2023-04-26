class A:
    def func_1(self):
        ...

    def func(self):
        return 1

class B:
    def func_2(self):
        ...

    def func(self):
        return 2

class C(A, B):
    pass


c = C()
c.