import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
  comb = combinations(a, i)
  for c in comb:
    total = sum(c)
    if total == s:
      ans += 1

print(ans)