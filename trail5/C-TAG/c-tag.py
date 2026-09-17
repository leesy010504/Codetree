from itertools import combinations

n, m = map(int, input().split())

a = [input() for _ in range(n)]
b = [input() for _ in range(n)]

answer = 0

for i, j, k in combinations(range(m), 3):
    a_com = set()

    for word in a:
        key = word[i] + word[j] + word[k]
        a_com.add(key)

    distinguish = True

    for word in b:
        key = word[i] + word[j] + word[k]

        if key in a_com:
            distinguish= False
            break

    if distinguish:
        answer += 1

print(answer)