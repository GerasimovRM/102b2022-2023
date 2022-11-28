a = 3
b = 3.4
st = "123"
c = True
print(type(a), type(b), type(c), type(st))


st = "123.0123"
n = int(float(st))
print(n)
print(type(n), type(st))

n = 23.5
st = str(n)
print(n + 1, st + "1")

# все что 0 и все что пустое => False, иначе к True
st = ""
a = 0
b = 0.0
print(a == b)
print(bool(st), bool(a), bool(b), bool(1), bool(-2.5), bool("0"))

print(bool(0), bool("0"))


