import sys

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort()

def dfs(v, visited, seq):
    visited[v] = 1
    seq.append(v)
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i, visited, seq) 
    return seq     

def bfs(start):
    q = [start]
    visited =[0] * (n+1)
    seq = [] * (n+1)

    while q:
        v = q.pop(0)
        seq.append(v)
        visited[v] = 1
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
    return seq

result_dfs = dfs(v, [0 for _ in range(n+1)], [])
result_bfs = bfs(v)

str1 = ' '.join(str(e) for e in result_dfs)
str2 = ' '.join(str(e) for e in result_bfs)

print(str1)
print(str2)
