class Time:
    def __init__(self, m, s):
        self.minutes = m + s // 60
        self.seconds = s % 60

    # a + 10
    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.minutes + other.minutes,
                        self.seconds + other.seconds)
        elif isinstance(other, int):
            return Time(self.minutes, self.seconds + other)
        else:
            return None

    # a += b
    def __iadd__(self, other):
        self.seconds += other.seconds
        self.minutes += other.minutes + self.seconds // 60
        self.seconds %= 60
        return self

    # 10 + a
    def __radd__(self, other):
        return Time.__add__(self, other)

    def __str__(self):
        return f"Время {self.minutes}:{self.seconds}"

    def __repr__(self):
        return f"Time({self.minutes}, {self.seconds})"
        # return str(self)  # self.__str__()

    # self < other
    def __lt__(self, other):
        return (self.minutes, self.seconds) < (other.minutes, other.seconds)


a = Time(6, 20)
b = Time(7, 50)
c = a + b
print(id(c))
c += b
print(id(c))
d = a + 10  # a.__add__(10)
e = 10 + a  # 10.__add__(a)
print(sorted([a, b, c, d, e]))
print(b < a)


