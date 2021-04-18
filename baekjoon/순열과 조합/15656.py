from itertools import product

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(product(a, repeat=m))
b.sort()
for x in b:
    print(*x)