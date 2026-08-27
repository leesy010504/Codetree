n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

s1 = set(arr1)
s2 = set(arr2)

print(' '.join('1' if x in s1 else '0' for x in arr2))