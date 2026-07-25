n = int(input())
words = [input() for _ in range(n)]

dic = {}

for i, word in enumerate(words):
    dic[word] = dic.get(word, 0) + 1

print(max(dic.values()))