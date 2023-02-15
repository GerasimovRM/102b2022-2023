d = {}
for _ in range(int(input())):
    x, y = input().split()
    t = (len(x), x[:-1], len(y), y[:-1])
    if t not in d:
        d[t] = 0
    d[t] += 1
print(max(d.values()))

