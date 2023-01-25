s1 = set()
s2 = set()
s3 = set()

for elem in s1, s2, s3:
    while True:
        st = input()
        if not st:
            break
        elem.add(st)


result = s1 ^ s2 ^ s3
# for elem in result:
#     print(elem)
print(*result, sep='\n')



