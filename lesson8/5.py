n = int(input())
s = set()
for _ in range(n):
    word = input()
    if word in s:
        print("ДА")
    else:
        print("НЕТ")
        s.add(word)
