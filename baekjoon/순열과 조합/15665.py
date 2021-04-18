from itertools import product

n, m = map(int, input().split())
a = list(map(int, input().split()))

b = sorted(list(set(product(a, repeat=m))))

for x in b:
    print(*x)