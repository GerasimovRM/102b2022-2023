lst = []
lst.append(1)
lst.append(lst)
print(lst, id(lst), id(lst[-1]))
lst2 = lst[-1]
print(lst is lst2)

