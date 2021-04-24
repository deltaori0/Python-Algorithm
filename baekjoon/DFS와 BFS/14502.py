import sys
import copy
from collections import deque
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

def bfs(b):
    cnt = 0
    chk = [[0] * m for _ in range(n)]
    q = deque()
    for v in virus:
        sx, sy = v
        chk[sx][sy] = 1
        q.append([sx, sy])

        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n : continue
                if ny < 0 or ny >= m : continue
                if b[nx][ny] == 1: continue
                if chk[nx][ny] != 0: continue

                b[nx][ny] = 2
                chk[nx][ny] = 1
                q.append([nx, ny])
        
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt
        



n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

virus = [[i, j] for i in range(n) for j in range(m) if a[i][j] == 2]
candidates = [[i, j] for i in range(n) for j in range(m) if a[i][j] == 0]

comb = list(combinations(candidates, 3))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maximum_safe = 0
for c in comb:
    b = copy.deepcopy(a)
    for x, y in c:
        b[x][y] = 1
    s = bfs(b)
    if s > maximum_safe:
        maximum_safe = s

print(maximum_safe)