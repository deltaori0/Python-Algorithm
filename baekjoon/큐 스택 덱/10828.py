import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = []

for _ in range(n):
    com, *num = input().split()

    if com == "push":
        s.append(num[0])
    elif com == "pop":
        print(s.pop() if s else -1)
    elif com == "size":
        print(len(s))
    elif com == "empty":
        print(1 if not s else 0)
    elif com == "top":
        print(s[-1] if s else -1)