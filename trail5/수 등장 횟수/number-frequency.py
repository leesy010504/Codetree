n, m = map(int, input().split())
arr = list(map(int, input().split()))
list_a = list(map(int,input().split()))

dic = {}

for elem in arr:
    dic[elem] = dic.get(elem, 0) + 1

print(*(dic.get(i, 0) for i in list_a))

