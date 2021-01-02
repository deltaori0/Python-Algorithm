from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    for i, p in enumerate(progresses):
        d = math.ceil((100 - p) / speeds[i])
        days.append(d)
        
    queue = deque(days)
    
    while queue:
        cur = queue.popleft()
        temp = queue.copy()
        cnt = 1
        for q in temp:
            if cur < q:
                break
            queue.popleft() 
            cnt += 1
        answer.append(cnt)
    return answer