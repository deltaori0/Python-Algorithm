from itertools import product

n, m = map(int, input().split())

a = list(product(range(1, n+1), repeat=m))

for x in a:
    print(*x)
