d = {}
words = input().split()
for word in words:
    if word not in d:
        d[word] = 0
    d[word] += 1
    print(d[word], end=' ')
