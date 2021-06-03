import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, x)
