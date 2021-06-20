import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check_ripe(a):
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                return False
    return True

def bfs(a):
    
    cnt = 0

    while q:
        for _ in range(len(q)): # 큐에 있는 모든 요소 제거 
            x, y = q.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= n: continue
                if ny < 0 or ny >= m: continue
                if a[nx][ny] != 0: continue
                if chk[nx][ny] != 0: continue
                
                chk[nx][ny] = 1
                a[nx][ny] = 1
                q.append([nx, ny])
            
        cnt += 1
        # print(a)

    if check_ripe(a):
        return cnt - 1
    else:
        return -1         

q = deque([])
chk = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append([i, j])
            chk[i][j] = 1

print(bfs(a))