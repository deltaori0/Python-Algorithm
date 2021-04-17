# import sys
# n = int(sys.stdin.readline())
# m = []
# for _ in range(n):
#     m.append(int(sys.stdin.readline()))

# m.sort()
# for i in m:
#     print(i)

# 새로운 방법
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
for x in a:
    print(x)