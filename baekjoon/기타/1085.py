import sys
input = lambda: sys.stdin.readline().rstrip()

x, y, w, h = map(int, input().split())

ans = min(abs(x-w), abs(y-h), abs(x), abs(y))

print(ans)