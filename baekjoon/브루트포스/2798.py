import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))

comb = list(map(sum, combinations(a, 3)))
result = filter(lambda x: x <= m, comb)
print(max(result))
