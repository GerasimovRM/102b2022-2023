a = 10
b = 10
break_all = False
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if j == 7:
            break_all = True
            break
        print(f"{i}+{j}={i + j}", end="\t")
    if break_all:
        break
    print()