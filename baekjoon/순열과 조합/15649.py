from itertools import permutations

n, m = map(int, input().split())

a = list(permutations(range(1, n+1), m))

for x in a:
    print(*x)