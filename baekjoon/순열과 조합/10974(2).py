from itertools import permutations as pm

n = int(input())
p = list(pm(range(1, n+1)))

for x in p:
    print(*x)