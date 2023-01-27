lst = [3, 2, 4, 7]
for elem in lst:
    if elem == 2:
        elem = 4
print(lst)
for i in range(len(lst)):
    if lst[i] == 2:
        lst[i] = 4
print(lst)

# for i in range(len(lst)):
#     if i == len(lst) - 1:
#         print(lst[i])
#     else:
#         print(lst[i], end='->')

lst = [3, 2, 4, 7]
for i, elem in enumerate(lst):
    print(i, elem)
