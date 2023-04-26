class A:
    def func(self):
        return 1




class B(A):
    def func(self):
        return 2

    def call_1(self):
        return self.func()

    def call_2(self):
        return super().func()




b = B()
print(b.call_1())
print(b.call_2())

a = A()
print(super().func())
