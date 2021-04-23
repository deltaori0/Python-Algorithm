import queue

# 최단거리 -> bfs 사용
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

# 4 방향 이동 (위-오른-아래-왼쪽)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
chk = [[0] * m for _ in range(n)]

q = queue.Queue()
q.put([0, 0])
chk[0][0] = 1


while not q.empty():
    x, y = q.get()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n: continue  # 1. 배열의 범위를 벗어나는지
        if ny < 0 or ny >= m: continue  # 1. 배열의 범위를 벗어나는지
        if a[nx][ny] == 0: continue     # 2. 벽인지 체크
        if chk[nx][ny] != 0: continue   # 3. 이미 방문한 곳인지 체크

        chk[nx][ny] = chk[x][y] + 1
        q.put([nx, ny])

print(chk[n-1][m-1])