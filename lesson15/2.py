lst = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst
print(lst == lst2, id(lst), id(lst2), lst is lst2)
print(lst is lst3)
