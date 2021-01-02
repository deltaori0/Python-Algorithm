v = int(input())
e = int(input())
# 일부러 v 개수보다 하나 더 많게 해서 0은 아예 신경 안 쓰도록!!
graph = [[0 for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# print(graph)

# 1번 노드와 연결된 모든 노드 뽑기
def bfs(graph, start):
    queue = [start]
    visited = []

    while queue:
        temp = queue.pop(0) # 가장 앞에 있는 원소 뽑기
        visited.append(temp)

        for i in range(1, v+1): # i는 1부터 7까지
            # temp와 i가 연결되어 있고
            # i는 처음 방문하는 노드이고
            # i가 큐에 없다면
            if graph[temp][i] == 1 and i not in visited and i not in queue:
                queue.append(i)
    # print(visited)
    return len(visited) - 1

print(bfs(graph, 1))