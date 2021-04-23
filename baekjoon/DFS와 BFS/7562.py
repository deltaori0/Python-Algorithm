from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()
t = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())

    a = [[0] * n for _ in range(n)]
    q = deque()
    a[sx][sy] = 1
    q.append([sx, sy])

    while q:
        x, y = q.popleft()
        if x == gx and y == gy:
            print(a[gx][gy]-1)
            break

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= n: continue
            if a[nx][ny] != 0: continue

            a[nx][ny] = a[x][y] + 1
            q.append([nx, ny])
    
        