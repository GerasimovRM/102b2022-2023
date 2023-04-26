with open("in.txt", "r") as f:
    # I
    data = list(map(lambda x: int(x) ** 2, f.read().split()))
    print(repr(data))
    f.seek(0)
    # II
    data = [int(line.strip()) ** 2 for line in f]
    print(data)
    f.seek(0)
    # III
    data = list(map(lambda x: int(x.strip()) ** 2, f.readlines()))
    print(data)

with open("result.txt", "w") as f:
    f.write('\n'.join(map(str, data)))
    f.writelines(map(lambda x: str(x) + '\n', data))
    print(*data, sep='\n', file=f)

