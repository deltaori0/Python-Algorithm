from itertools import permutations

n, m = map(int, input().split())
a = list(map(int, input().split()))

b = list(permutations(a, m))
b.sort()

for x in b:
    cur = x[0]
    for i in range(1, m):
        if x[i] < cur:
            break
        cur = x[i]
    else:
        print(*x)