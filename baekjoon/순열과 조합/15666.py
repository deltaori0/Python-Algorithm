from itertools import combinations_with_replacement as com

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = sorted(list(set(com(a, m))))

for x in b:
    print(*x)