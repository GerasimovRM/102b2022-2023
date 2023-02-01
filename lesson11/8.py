data = input().split(', ')
new_data = ["flower" if i % 2 == 0 else "gemstone"for i in range(len(data))]
print('; '.join(new_data))
