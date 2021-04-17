import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append([x, y])

a.sort(key=lambda x: (x[1], x[0]))

for x in a:
    print(x[0], x[1])