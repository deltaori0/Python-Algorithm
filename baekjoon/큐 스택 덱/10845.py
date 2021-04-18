import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
queue = []

for _ in range(n): 
    command = input().split()
    if command[0] == "push":
        num = command[1]
        queue.append(num)
    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            num = queue.pop(0)
            print(num)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])