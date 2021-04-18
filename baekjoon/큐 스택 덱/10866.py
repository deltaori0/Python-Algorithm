from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dq = deque()

for _ in range(n):
    com, *num = input().split()
    if com == "push_front":
        dq.appendleft(int(num[0]))
    elif com == "push_back":
        dq.append(int(num[0]))
    elif com == "pop_front":
        print(dq.popleft() if dq else -1)
    elif com == "pop_back":
        print(dq.pop() if dq else -1)
    elif com == "size":
        print(len(dq))
    elif com == "empty":
        print(1 if not dq else 0)
    elif com == "front":
        print(dq[0] if dq else -1)
    elif com == "back":
        print(dq[-1] if dq else -1)