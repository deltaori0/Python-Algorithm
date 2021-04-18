from itertools import combinations_with_replacement as com

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = list(com(a, m))

for x in b:
    cur = x[0]
    for i in range(1, m):
        if x[i] < cur:
            break
        cur = x[i]
    else:
        print(*x)