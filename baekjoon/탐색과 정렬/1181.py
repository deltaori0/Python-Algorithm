import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [input() for _ in range(n)]
a = list(set(a))

a.sort(key=lambda x: (len(x), x))

for x in a:
    print(x)