import sys
from itertools import combinations as com
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

c = list(com(range(1, n+1), m))

for x in c:
    print(*x)