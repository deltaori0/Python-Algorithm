from itertools import combinations_with_replacement as com
n, m = map(int, input().split())

a = list(com(range(1, n+1), m))

for x in a:
    print(*x)