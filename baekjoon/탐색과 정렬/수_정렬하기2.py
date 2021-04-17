import sys
n = int(sys.stdin.readline())
m = []
for _ in range(n):
    m.append(int(sys.stdin.readline()))

m.sort()
for i in m:
    print(i)