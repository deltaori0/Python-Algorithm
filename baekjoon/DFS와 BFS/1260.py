import queue
# 정점 개수, 간선 개수, 시작 정점 번호
n, m, v = map(int, input().split())

# 그래프 입력 (인접리스트 방식)
a = [list() * (n+1) for _ in range(n+1)]

# 간선 정보 입력받기
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

# 오름차순 정렬 (정점을 작은 순서대로 방문하므로)
for x in a:
    x.sort()

# BFS 구현
# 체크는 큐에서 뺄 때가 아니라 들어갈 때 체크해주기
def bfs(v):
    q = queue.Queue()
    q.put(v)
    chk[v] = True

    while not q.empty():
        now = q.get()
        print(now, end=' ')

        for next in a[now]:
            if not chk[next]:
                chk[next] = True
                q.put(next)
        
    print()

# DFS 구현
def dfs(node):
    chk[node] = True
    print(node, end=' ')

    for next in a[node]:
        if not chk[next]:
            dfs(next)

# 체크 배열을 dfs, bfs 하기 직전에 각각 선언해 줘야 한다
# 한 번 돌리고 나서 다시 False로 초기화 시켜줘야 하기 때문
chk = [False] * (n+1)
dfs(v)
print()
chk = [False] * (n+1)
bfs(v)