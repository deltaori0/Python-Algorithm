# import sys
# # n, m = map(int, input().split())
# n ,m = map(int,sys.stdin.readline().split())
# graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

# for _ in range(m):
#     # x, y = map(int, input().split())
#     x, y = map(int,sys.stdin.readline().split())
#     graph[x][y] = 1
#     graph[y][x] = 1

# def count_connected():
#     visited = [0] * (n+1)

#     for i in range(1, n+1):
#         if visited[i] == 0:
#             bfs(i)
#             count += 1
#     return count
    

# def bfs(start):
#     queue = [start]
#     visited = []

#     while queue:
#         temp = queue.pop(0)
#         visited.append(temp)  
#         for i in range(1, n+1):
#             if graph[temp][i] == 1 and i not in visited and i not in queue:
#                 queue.append(i)

#     return visited

# print(count_connected(graph))   

import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)

def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        count+=1

print(count)