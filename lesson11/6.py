lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [elem ** 2 for elem in lst if elem % 2 == 1]
print(lst2)