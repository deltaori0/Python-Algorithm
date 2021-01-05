from collections import deque
def solution(n, computers):
    answer = 0
    
    queue = deque()
    visited = [0 for _ in range(n)]
    
    count = 0
    
    while 0 in visited:
        idx = visited.index(0)
        queue.append(idx)
        visited[idx] = 1
        count += 1
        
        while queue:
            temp = queue.popleft()
            for i in range(n):
                if computers[temp][i] == 1 and visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
    
    answer = count
    return answer