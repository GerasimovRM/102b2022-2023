lst = [1, 2, 3]
# for elem in lst:
#     print(elem)

it = iter(lst)
while True:
    try:
        elem = next(it)
        print(elem)
    except StopIteration:
        break
    