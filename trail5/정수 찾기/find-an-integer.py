n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

print('\n'.join('1' if x in a else '0' for x in b))