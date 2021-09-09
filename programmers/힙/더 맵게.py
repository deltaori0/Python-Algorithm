import heapq

def solution(scoville, K):
    cnt = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        
        if a > K:
            return cnt
        
        b = heapq.heappop(scoville)

        heapq.heappush(scoville, a + b * 2)
        cnt += 1
    
    if heapq.heappop(scoville) < K:
        return -1
    else:
        return cnt