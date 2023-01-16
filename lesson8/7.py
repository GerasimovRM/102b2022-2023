word1 = set(input())
word2 = set(input())
word3 = set(input())
result = (word1 & word2) | (word1 & word3) | (word2 & word3)
print(*result, sep='')

