import queue

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, input().split())

    if not w and not h: break
    a = [list(map(int, input().split())) for _ in range(h)]
    q = queue.Queue()
    total = 0

    for i in range(h):
        for j in range(w):
            if a[i][j] == 1:
                a[i][j] = 2 # 방문했다는 표시로 2로 바꿔준다
                q.put([i, j])

                # 그 위치에서부터 BFS 탐색
                while not q.empty():
                    x, y = q.get()

                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >= h: continue
                        if ny < 0 or ny >= w: continue
                        if a[nx][ny] == 0: continue # 바다
                        if a[nx][ny] == 2: continue # 이미 방문했던 곳

                        a[nx][ny] = 2
                        q.put([nx, ny])

                total += 1

    print(total)
            
