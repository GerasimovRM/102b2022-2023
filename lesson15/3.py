lst = []
# lst.append(0)
# lst.append(lst)
# lst.append(lst)
# lst.append(2)
lst.extend([0, lst, lst, 2])
print(lst)