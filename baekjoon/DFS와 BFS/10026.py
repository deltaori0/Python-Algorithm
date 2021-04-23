import queue

n = int(input())
a = [list(input()) for _ in range(n)]


def bfs(a):
    q = queue.Queue()
    chk = [[0]*n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    total = 0
    # 적록색맹 아닌 사람
    for i in range(n):
        for j in range(n):
            if chk[i][j] == 0:
                chk[i][j] = 1
                q.put([i, j])

                while not q.empty():
                    x, y = q.get()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >= n: continue
                        if ny < 0 or ny >= n: continue
                        if a[nx][ny] != a[x][y]: continue
                        if chk[nx][ny] != 0: continue

                        chk[nx][ny] = 1
                        q.put([nx, ny])
                total += 1
    return total

print(bfs(a), end=' ')
b = a[:]
for i in range(n):
    for j in range(n):
        if b[i][j] == 'G':
            b[i][j] = 'R'
print(bfs(b))
