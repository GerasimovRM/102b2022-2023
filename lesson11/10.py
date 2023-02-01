substr = input()
lst = input().split()
lst = [elem for elem in lst if substr in elem]
print(" ".join(lst))