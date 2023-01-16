s1 = set()
s2 = set()
s3 = set()

while True:
    st = input()
    if not st:
        break
    s1.add(st)

while True:
    st = input()
    if not st:
        break
    s2.add(st)

while True:
    st = input()
    if not st:
        break
    s3.add(st)

result = s1 ^ s2 ^ s3
# for elem in result:
#     print(elem)
print(*result, sep='\n')



