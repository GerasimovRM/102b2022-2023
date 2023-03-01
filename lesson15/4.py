def mirror(arr_):
    global arr
    mirrored_part = arr_.copy()  # arr[:]
    mirrored_part.reverse()
    arr = arr_ + mirrored_part


array = [1, 2]
mirror(array)
print(array)
print(arr)