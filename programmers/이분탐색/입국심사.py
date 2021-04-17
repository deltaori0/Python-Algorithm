def solution(n, times):
    answer = 0
    times.sort()

    left = 1
    right = times[-1] * n 

    while left <= right:
        middle = (left + right) // 2
        m = 0
        for t in times:
            m += middle // t
        if m >= n:  # n명을 심사할 수 있는 경우 최소를 구하기 위해 시간을 줄여본다
            answer = middle
            right = middle - 1
        else: 
            left = middle + 1                  
    return answer