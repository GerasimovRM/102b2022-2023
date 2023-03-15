line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
matrix = [line1, line2, line3]
sums = list(map(lambda x: sum(x), matrix))
transpose = list(zip(*matrix))
sums_t = list(map(lambda x: sum(x), transpose))
s = sums + sums_t
if len(set(s)) == 1:
    print("YES")
else:
    print("NO")