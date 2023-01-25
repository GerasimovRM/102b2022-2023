lst = []
for _ in range(int(input())):
    lst.append(input())
k = int(input()) - 1
for elem in lst:
    print(elem[k], end='')
