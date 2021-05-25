from collections import deque
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

temp = [[i, j] for i in range(n) for j in range(n) if a[i][j] == 9]
shark = temp[0]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

a[shark[0]][shark[1]] = 0

shark_size = 2; now_eat = 0; time = 0

def bfs(shark):
    q = deque()
    chk = [[0] * n for _ in range(n)]
    chk[shark[0]][shark[1]] = 1
    q.append([shark[0], shark[1]])

    while q:
        fish = []
        q_size = len(q)

        for _ in range(q_size):
            x, y = q.popleft()
            # print("x", x, "y", y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                print("nx", nx, "ny", ny)

                if nx < 0 or nx >= n: continue
                if ny < 0 or ny >= n: continue
                if chk[nx][ny]: continue

                if 0 < a[nx][ny] < shark_size:
                    fish.append([nx, ny])
                else:
                    chk[nx][ny] = chk[x][y] + 1
                    q.append([nx, ny])
            
            if fish:
                fish.sort()
                print("fish", fish)
                a[fish[0][1], fish[0][1]] = 0
                return fish[0], chk[x][y]
            return 0, 0
    
while True:
    shark, t = bfs(shark)
    print("shark", shark, "t", t)
    if t == 0:
        break
    time += t
    now_eat += 1
    if shark_size == now_eat:
        shark_size += 1
        now_eat = 0

print(time)