import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

while True:
    k, *a = map(int, input().split())
    if k == 0:
        break
    c = list(combinations(a, 6))

    for x in c:
        print(*x)
    print()