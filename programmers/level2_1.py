# Finn 수학 공부

def solution(n):
    answer = 0
    cur = 0
    
    for i in range(1, n+1):
        cur = 0
        for j in range(i, n+1):
            cur += j
            if cur == n:
                answer += 1
                break
            elif cur > n:
                break
    return answer