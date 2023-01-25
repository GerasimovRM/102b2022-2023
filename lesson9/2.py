lst = []
lst.append(3)
lst.append(4)
lst.append(5)
print(lst)
elem = lst.pop(1)
print(elem, lst)

lst = []
for i in range(1, 21):
    lst.append(i ** 2)
print(lst)
print(lst[-2], lst[1])
print(lst[::2])
print(lst[::-1])
