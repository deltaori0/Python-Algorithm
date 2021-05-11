import sys
import queue
input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())
a = [list(map(int, input())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start):
    q = queue.Queue()
    chk = [[False] * n for _ in range(m)]
    q.put(start)
    chk[start[0]][start[1]] = True

    while not q.empty():
        x, y = q.get()
        if x == m-1: return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m: continue
            if ny < 0 or ny >= n: continue
            if a[nx][ny] == 1: continue
            if chk[nx][ny]: continue

            chk[nx][ny] = True
            q.put([nx, ny])
    
    return False




for i in range(n):
    if a[0][i] == 0:
        if bfs([0, i]):
            print('YES')
            break
else:
    print('NO')

        