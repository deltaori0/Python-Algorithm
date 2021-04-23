import queue

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = queue.Queue()
chk = [[0] * m for _ in range(n)]

total = 0
maximum_size = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and chk[i][j] == 0:
            size = 1
            chk[i][j] = 1
            q.put([i, j])

            while not q.empty():
                x, y = q.get()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n: continue
                    if ny < 0 or ny >= m: continue
                    if a[nx][ny] == 0: continue
                    if chk[nx][ny] != 0: continue
                    size += 1
                    chk[nx][ny] = 1
                    q.put([nx, ny])
            if size > maximum_size:
                maximum_size = size
            total += 1

print(total)
print(maximum_size)