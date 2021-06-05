import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    prev = [1, 0]
    cur = [1, 0]
    for i in range(1, N+1):
        if i == 1:
            cur[0], cur[1] = 0, 1
        else:
            temp_0, temp_1 = prev[0], prev[1]
            prev[0], prev[1] = cur[0], cur[1]
            cur[0] += temp_0
            cur[1] += temp_1
    print(cur[0], cur[1])
            
