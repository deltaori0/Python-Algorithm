import queue
n = int(input())
a = [list(map(int, input())) for _ in range(n)]
q = queue.Queue()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            a[i][j] = 2 # 방문 표시
            q.put([i, j])

            total = 0
            while not q.empty():
                total += 1
                x, y = q.get()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n: continue
                    if ny < 0 or ny >= n: continue
                    if a[nx][ny] == 0: continue
                    if a[nx][ny] == 2: continue

                    a[nx][ny] = 2
                    q.put([nx, ny])
            ans.append(total)
ans.sort()
print(len(ans))
for x in ans:
    print(x)


