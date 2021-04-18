import sys
import queue
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = queue.Queue()

for _ in range(n):
    com, *num = input().split()
    if com == "push":
        q.put(int(num[0]))
    elif com == "pop":
        print(q.get() if not q.empty() else -1)
    elif com == "size":
        print(q.qsize())
    elif com == "empty":
        print(1 if q.empty() else 0)
    elif com == "front":
        print(q.queue[0] if not q.empty() else -1)
    elif com == "back":
        print(q.queue[-1] if not q.empty() else -1)