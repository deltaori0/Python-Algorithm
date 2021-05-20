import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

a.reverse()

cnt = 0
for x in a:
    if x > k:
        continue
    div, mod = divmod(k, x)
    cnt += div
    k = mod

print(cnt)