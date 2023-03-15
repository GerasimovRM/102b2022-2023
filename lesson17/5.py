import time
print(time.time())
lst =list(range(10000000))
t1 = time.time()
lst2 = [elem ** 2 for elem in lst]
t2 = time.time()
for i in lst2:
    print(i)
t3 = time.time()
lst3 = []
for i in range(len(lst)):
    lst3.append(lst[i] ** 2)
t4 = time.time()
for i in lst3:
    print(i)
t5 = time.time()
lst4 = map(lambda x: x ** 2, lst)
t6 = time.time()
for i in lst4:
    print(i)
