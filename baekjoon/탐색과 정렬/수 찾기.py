import sys
n = int(input())
a = set(sys.stdin.readline().split())
m = int(input())
b = sys.stdin.readline().split()

for i in b:
    if i in a:
        print(1)
    else:
        print(0)