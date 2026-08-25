from collections import Counter

s = input()
cnt = Counter(s)

for ch in s:
    if cnt[ch] == 1:
        print(ch)
        break
else:
    print(None)