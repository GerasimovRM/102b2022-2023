n = int(input())
s = set()
for _ in range(n):
    st = input()
    s1 = set(st)
    s |= s1
print(len(s))

