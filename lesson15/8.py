d = {i: str(i) for i in range(0, 10)}
d.update({10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"})
print(d)


def from_dec_to_hex(number):
    result = ''
    while number != 0:
        result += d[number % 16]
        number //= 16
    return result[::-1]


def rgb(r, g, b):
    t = [r, g, b]
    for i in range(3):
        if t[i] < 0:
            t[i] = 0
        elif t[i] > 255:
            t[i] = 255
    r, g, b = t
    r, g, b = from_dec_to_hex(r).zfill(2), \
        from_dec_to_hex(g).zfill(2), \
        from_dec_to_hex(b).zfill(2)
    return r + g + b


print(rgb(250, 240, 190))
