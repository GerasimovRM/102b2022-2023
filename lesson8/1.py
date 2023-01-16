
s1 = {1, 2, 3, 3, 2}
s2 = {3, 4, 5, 9}
print(s1 | s2, s1.union(s2))
print(s1 & s2, s1.intersection(s2))
print(s1 - s2, s1.difference(s2))
print(s1 ^ s2, s1.symmetric_difference(s2))

s3 = {4, 5, 6}
s4 = {4, 5, 6}
print(s3 == s4, s3 is s4, id(s3), id(s4))
print(id(s3))
s3 |= {2, 3, 4}
print(id(s3))
s3.intersection_update({2, 3, 4})
s3 = s3 | {2, 3, 4}
print(id(s3))


