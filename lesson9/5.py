lst = []
n = int(input())
for i in range(n):
    st = input()
    lst.append(st)

find_word = input()
# for i in range(len(lst)):
#     if find_word in lst[i]:
#         print(lst[i])
for elem in lst:
    if find_word in elem:
        print(elem)
x
