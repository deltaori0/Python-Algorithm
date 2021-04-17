from collections import deque

def is_highest_priority(cur_p, queue):
    for (i, p) in queue:
        if cur_p < p:
            return False
    return True
        
def solution(priorities, location):
    count = 0
    
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    seq = []
    
    while queue:
        cur_i, cur_p = queue.popleft()
        
        if not is_highest_priority(cur_p, queue):
            queue.append((cur_i, cur_p))
            continue
        
        seq.append(cur_i)
    
    answer = seq.index(location) + 1             
    return answer